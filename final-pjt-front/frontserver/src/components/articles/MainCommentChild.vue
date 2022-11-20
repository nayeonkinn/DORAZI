<template>
  <div>
    ㄴ<span @click="goProfile(child.user.username)">{{
      child.user.username
    }}</span>
    -
    <span v-if="!updateOn">
      <span v-if="child.mention_to">@{{ child.mention_to }} </span
      >{{ child.content }}
      <button @click="likeComment(articleId, child.id)">
        {{ commentMsg(child) }}
      </button>
      <span> {{ child.like_users.length }} </span>
      <span> {{ commentCreatedAt(child) }} </span>
      <button @click="childChildDivToggle">답글 달기</button>
      <span v-if="child.user.id === userId">
        <button @click="updateOnToggle">수정</button>
        <button @click="deleteComment">삭제</button>
      </span>
    </span>

    <span v-else>
      <textarea
        cols="40"
        rows="1"
        :value="child.content"
        @input="updateInput"
        @keyup.enter="updateComment"
      ></textarea>
      <button @click="updateComment">수정</button>
      <button @click="updateOnToggle">취소</button>
    </span>

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
      child2: null,
      childChildDiv: false,
      childChildComment: null,
      updateOn: false,
      updateCommentData: null,
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
          this.$emit("create-child-child-comment", response.data);
        })
        .catch((error) => {
          console.log(error);
        });

      this.childChildComment = null;
      this.childChildDiv = false;
    },
    updateOnToggle() {
      this.updateOn = !this.updateOn;
    },
    updateInput(event) {
      this.updateCommentData = event.target.value;
    },
    updateComment() {
      axios({
        method: "PUT",
        url: `${API_URL}/articles/${this.articleId}/comment/${this.child.id}/`,
        headers: {
          Authorization: `Token ${this.token}`,
        },
        data: {
          content: this.updateCommentData,
        },
      })
        .then((response) => {
          // console.log(response);
          this.$emit('update-child-comment', this.child.id, response.data)
          this.updateOnToggle();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    deleteComment() {
      axios({
        method: "DELETE",
        url: `${API_URL}/articles/${this.articleId}/comment/${this.child.id}/`,
        headers: {
          Authorization: `Token ${this.token}`,
        },
        data: {
          content: this.updateCommentData,
        },
      })
        .then(() => {
          // console.log(response);
          this.$emit("delete-child-comment", this.child.id);
        })
        .catch((error) => {
          console.log(error);
        });
    },

  },
  created() {
      this.child2 = this.child
  }
};
</script>

<style>
</style>