<template>
  <div>
    ㄴ<span @click="goProfile(child.user.username)">{{
      child.user.username
    }}</span>
    - <span v-if="child.mention_to">@{{ child.mention_to }} </span
    >{{ child.content }}
    <button @click="likeComment(articleId, child.id)">
      {{ commentMsg(child) }}
    </button>
    <span> {{ child.like_users.length }} </span>
    <span> {{ commentCreatedAt(child) }} </span>
    <button @click="childChildDivToggle">답글 달기</button>

    <div v-if="childChildDiv">
      <textarea
        v-model="childChildComment"
        @keyup.enter="createChildChildComment"
        cols="40"
        rows="1"
      ></textarea>
      <button type="button" @click="createChildChildComment">등록</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MainArticleChildCommentList",
  props: {
    child: Object,
    articleId: Number,
  },
  data() {
    return {
      childChildDiv: false,
			childChildComment: null,
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
          // console.log(response);
          this.$emit("like-child-comment", commentId, response.data);
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
    childChildDivToggle() {
      this.childChildDiv = !this.childChildDiv;
    },
		createChildChildComment() {
      axios({
        method: "POST",
        url: `${API_URL}/articles/${this.articleId}/comment_create/${this.child.id}/comment_create/`,
        headers: {
          Authorization: `Token ${this.token}`,
        },
        data: {
          content: this.childChildComment,
        },
      })
        .then((response) => {
          // console.log(response);
					this.$emit('create-child-child-comment', response.data)
        })
        .catch((error) => {
          console.log(error);
        });

      this.childChildComment = null;
		}
  },
};
</script>

<style>
</style>