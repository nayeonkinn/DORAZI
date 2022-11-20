<template>
  <div v-if="!comment2.parent_comment">
    <span @click="goProfile(comment2.user.username)">
      {{ comment2.user.username }} </span
    >- {{ comment2.content }}
    <button @click="likeComment(comment2.article, comment2.id)">
      {{ commentMsg(comment2) }}
    </button>
    <span> {{ comment2.like_users.length }} </span>
    <span> {{ commentCreatedAt(comment2) }} </span>
    <button @click="childDivToggle">답글 달기</button>

    <div v-if="childDiv">
      <textarea
        v-model="childComment"
        @keyup.enter="createChildComment"
        cols="40"
        rows="1"
      ></textarea>
      <button type="button" @click="createChildComment">등록</button>
    </div>

    <MainArticleChildCommentList
      v-for="child in comment2.child_comment"
      :key="`comment-${child.id}`"
      :child="child"
      :articleId="comment2.article"
      @like-child-comment="likeChildComment"
			@create-child-child-comment="createChildChildComment"
    />
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";

import MainArticleChildCommentList from "@/components/articles/MainArticleChildCommentList";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MainArticleCommentList",
  components: {
    MainArticleChildCommentList,
  },
  props: {
    comment: Object,
    articleId: Number,
  },
  data() {
    return {
      comment2: null,
      childDiv: false,
      childComment: null,
    };
  },
  computed: {
    token() {
      return this.$store.state.token;
    },
    userId() {
      return this.$store.state.userId;
    },
  },
  methods: {
    goProfile(username) {
      this.$router.push({
        name: "ProfileView",
        params: {
          username: username,
        },
      });
    },
    likeComment(articleId, commentId) {
      axios({
        method: "post",
        url: `${API_URL}/articles/${articleId}/comment/${commentId}/like/`,
        headers: {
          Authorization: `Token ${this.token}`,
        },
      })
        .then((response) => {
          // console.log(response)
          this.comment2 = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    commentMsg(comment) {
      return comment.like_users.includes(this.userId) ? "♥" : "♡";
    },
    commentCreatedAt(comment) {
      return moment(String(comment.created_at)).format("YYYY-MM-DD HH:mm");
    },
    childDivToggle() {
      this.childDiv = !this.childDiv;
    },
    createChildComment() {
      axios({
        method: "POST",
        url: `${API_URL}/articles/${this.articleId}/comment_create/${this.comment2.id}/comment_create/`,
        headers: {
          Authorization: `Token ${this.token}`,
        },
        data: {
          content: this.childComment,
        },
      })
        .then((response) => {
          // console.log(response);
          this.comment2.child_comment.push(response.data);
        })
        .catch((error) => {
          console.log(error);
        });

      this.childComment = null;
    },
    likeChildComment(childCommentId, childCommentData) {
      this.comment2.child_comment = this.comment2.child_comment.map((child) => {
        if (child.id === childCommentId) {
          return childCommentData;
        } else {
          return child;
        }
      });
    },
		createChildChildComment(childChildComment) {
			this.comment2.child_comment.push(childChildComment);
		}
  },
  created() {
    this.comment2 = this.comment;
  },
};
</script>

<style>
</style>