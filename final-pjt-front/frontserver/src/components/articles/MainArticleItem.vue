<template>
  <div>
    <img
      :src="poster_path"
      alt="poster_img"
      style="width: 200px; height: 300px"
    />
    <h3>{{ article.user.username }}</h3>
    <p>{{ article_created_at }}</p>
    <p>{{ article.rating }}</p>
    <p>{{ article.content }}</p>
    <button @click="like">{{ likeMsg }}</button>
    <button @click="likeDivToggle">좋아요 {{ likeCount }}</button>
    <button @click="commentDivToggle">댓글 {{ commentCount }}</button>
    <div v-if="likeDiv">
      <div v-for="user in likeUsers" :key="`user-${user.id}`">
        <p>{{ user.username }}</p>
      </div>
    </div>
    <div v-if="commentDiv">
      <div v-for="comment in comments" :key="`comment-${comment.id}`">
        <p v-if="!comment.parent_comment">
          {{ comment.user.username }} - {{ comment.content }}
					<button @click="likeComment(comment.id)">{{ commentMsg(comment) }} {{ comment.like_users.length }}</button>
        </p>
      </div>
    </div>
    <hr />
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MainArticleItem",
  props: {
    article: Object,
  },
  data() {
    return {
      isLiked: null,
      likeCount: null,
      likeDiv: false,
      likeUsers: null,
      commentDiv: false,
      commentCount: null,
      comments: null,
    };
  },
  computed: {
    token() {
      return this.$store.state.token;
    },
    userId() {
      return this.$store.state.userId;
    },
    article_created_at() {
      return moment(String(this.article.created_at)).format("YYYY-MM-DD HH:mm");
    },
    poster_path() {
      return (
        "https://image.tmdb.org/t/p/original/" + this.article.movie.poster_path
      );
    },
    likeMsg() {
      return this.isLiked ? "♥" : "♡";
    },
  },
  methods: {
    setLikeData(article) {
      const likeUsers = article.like_users;
      this.isLiked = likeUsers.some((user) => user.id === this.userId);
      this.likeCount = likeUsers.length;
      this.likeUsers = article.like_users;
    },
    setCommentsData(article) {
			this.comments = article.articlecomment_set;
      this.commentCount = article.articlecomment_set.length;
    },
    like() {
      axios({
        method: "post",
        url: `${API_URL}/articles/${this.article.id}/like/`,
        headers: {
          Authorization: `Token ${this.token}`,
        },
      })
        .then((response) => {
          // console.log(response)
          this.setLikeData(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
			},
			likeComment(commentId) {
				axios({
					method: "post",
					url: `${API_URL}/articles/${this.article.id}/comment/${commentId}/like/`,
					headers: {
						Authorization: `Token ${this.token}`,
					},
				})
					.then((response) => {
						// console.log(response)
						this.comments.forEach((comment) => {
							if (comment.id === commentId) {
								const index = this.comments.indexOf(comment)
								this.comments.splice(index, 1, response.data)
							}
						});
					})
					.catch((error) => {
						console.log(error);
					});
		},
    likeDivToggle() {
      this.likeDiv = !this.likeDiv;
    },
    commentDivToggle() {
      this.commentDiv = !this.commentDiv;
    },
		commentMsg(comment) {
			return comment.like_users.includes(this.userId)? "♥" : "♡";
		}
  },
  created() {
    this.setLikeData(this.article);
    this.setCommentsData(this.article);
  },
};
</script>

<style>
</style>