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

    <div v-if="userId === article.user.id">
      <button>수정</button>
      <button @click="deleteArticle">삭제</button>
    </div>

    <button @click="like">{{ likeMsg }}</button>
    <button @click="likeDivToggle">좋아요 {{ likeCount }}</button>
    <button @click="commentDivToggle">댓글 {{ commentCount }}</button>

    <div v-if="likeDiv">
      <div v-for="user in likeUsers" :key="`user-${user.id}`">
        <p @click="goProfile(user.username)">{{ user.username }}</p>
      </div>
    </div>

    <div v-if="commentDiv">
      <MainCommentList
        v-for="comment in comments"
        :key="`comment-${comment.id}`"
        :comment="comment"
        :articleId="article.id"
        @like-comment="likeComment"
        @update-comment="updateComment"
        @delete-comment="deleteComment"
        @like-child-comment="likeChildComment"
        @create-child-comment="createChildComment"
        @create-child-child-comment="createChildChildComment"
        @delete-child-comment="deleteChildComment"
      />
      <MainCommentForm
        :articleId="article.id"
        @create-comment="createComment"
      />
    </div>
    <hr />
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";

import MainCommentList from "@/components/articles/MainCommentList";
import MainCommentForm from "@/components/articles/MainCommentForm";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MainArticleItem",
  components: {
    MainCommentList,
    MainCommentForm,
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
    commentCount() {
      return this.comments.length;
    },
  },
  methods: {
    setLikeData(article) {
      const likeUsers = article.like_users;
      this.isLiked = likeUsers.some((user) => user.id === this.userId);
      this.likeCount = likeUsers.length;
      this.likeUsers = article.like_users;
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
    createComment(comment) {
      this.comments.push(comment);
    },
    updateComment(commentId, commentData) {
      this.comments = this.comments.map((comment) => {
        if (comment.id === commentId) {
          return commentData;
        } else {
          return comment;
        }
      });
    },
    likeComment(commentId, commentData) {
      this.comments = this.comments.map((comment) => {
        if (comment.id === commentId) {
          return commentData;
        } else {
          return comment;
        }
      });
    },
    deleteComment(commentId) {
      this.comments = this.comments.filter((comment) => {
        return comment.id != commentId;
      });
    },
    likeChildComment(commentId, commentData) {
      this.comments = this.comments.map((comment) => {
        if (comment.id === commentId) {
          const newComment = comment;
          newComment.child_comment = commentData;
          return newComment;
        } else {
          return comment;
        }
      });
    },
    createChildChildComment(commentId, commentData) {
      this.comments = this.comments.map((comment) => {
        if (comment.id === commentId) {
          const newComment = comment;
          newComment.child_comment = commentData;
          return newComment;
        } else {
          return comment;
        }
      });
      this.comments.push(commentData);
    },
    deleteChildComment(commentId, commentData, childId) {
      this.comments = this.comments.map((comment) => {
        if (comment.id === commentId) {
          const newComment = comment;
          newComment.child_comment = commentData;
          return newComment;
        } else {
          return comment;
        }
      });
      this.comments = this.comments.filter((comment) => {
        return comment.id !== childId;
      });
    },
    createChildComment(commentId, commentData) {
      this.comments.forEach((comment) => {
        if (comment.id === commentId) {
          comment.child_comment.push(commentData);
        }
      });
      this.comments.push(commentData);
    },
    deleteArticle() {
      axios({
        method: "delete",
        url: `${API_URL}/articles/${this.article.id}/`,
        headers: {
          Authorization: `Token ${this.token}`,
        },
      })
        .then(() => {
          // console.log(response)
          this.$emit('delete-article', this.article.id)
        })
        .catch((error) => {
          console.log(error);
        });
    },
    // 영민이가 수정 모달로 해준다
  },
  created() {
    // console.log(this.article)
    this.setLikeData(this.article);
    this.comments = this.article.articlecomment_set;
  },
};
</script>

<style>
</style>