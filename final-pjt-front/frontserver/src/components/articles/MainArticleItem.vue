<template>
  <div>
    <img
      :src="poster_path"
      alt="poster_img"
      style="width: 200px; height: 300px"
    />
    <h3 @click="goProfile(article.user.username)">
      {{ article.user.username }}
    </h3>
    <p>{{ article_created_at }}</p>
    <p>{{ article.rating }}</p>
    <p>{{ article.content }}</p>
    <button @click="like">{{ likeMsg }}</button>
    <button @click="likeDivToggle">좋아요 {{ likeCount }}</button>
    <button @click="commentDivToggle">댓글 {{ commentCount }}</button>
    <div v-if="likeDiv">
      <div v-for="user in likeUsers" :key="`user-${user.id}`">
        <p @click="goProfile(user.username)">{{ user.username }}</p>
      </div>
    </div>
    <div v-if="commentDiv">
      <MainArticleCommentList
        v-for="comment in comments"
        :key="`comment-${comment.id}`"
        :comment="comment"
      />
    </div>
    <hr />
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";

import MainArticleCommentList from "@/components/articles/MainArticleCommentList";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MainArticleItem",
  components: {
    MainArticleCommentList,
  },
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
    likeDivToggle() {
      if (this.commentDiv) {
        this.commentDiv = !this.commentDiv;
      }
      this.likeDiv = !this.likeDiv;
    },
    commentDivToggle() {
      if (this.likeDiv) {
        this.likeDiv = !this.likeDiv;
      }
      this.commentDiv = !this.commentDiv;
    },
    goProfile(username) {
      this.$router.push({
        name: "ProfileView",
        params: {
          username: username,
        },
      });
    },
  },
  created() {
    this.setLikeData(this.article);
    this.setCommentsData(this.article);
  },
};
</script>

<style>
</style>