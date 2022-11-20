<template>
  <div v-if="!comment.parent_comment">
    <span @click="goProfile(comment.user.username)">
      {{ comment.user.username }} </span
    >-
    <span v-if="!updateOn"
      >{{ comment.content }}
      <button @click="likeComment(comment.article, comment.id)">
        {{ commentMsg(comment) }}
      </button>
      <span> {{ comment.like_users.length }} </span>
      <span> {{ commentCreatedAt(comment) }} </span>
      <button @click="childDivToggle">답글 달기</button>
      <span v-if="comment.user.id === userId">
        <button @click="updateOnToggle">수정</button>
        <button @click="deleteComment">삭제</button>
      </span>
    </span>
    <span v-else>
      <textarea
        cols="40"
        rows="1"
        :value="comment.content"
        @input="updateInput"
        @keyup.enter="updateComment"
      ></textarea>
      <button @click="updateComment">수정</button>
      <button @click="updateOnToggle">취소</button>
    </span>

    <div v-if="childDiv">
      <textarea
        v-model="childComment"
        @keyup.enter="createChildComment"
        cols="40"
        rows="1"
      ></textarea>
      <button type="button" @click="createChildComment">등록</button>
    </div>

    <MainCommentChild
      v-for="child in comment.child_comment"
      :key="`comment-${child.id}`"
      :child="child"
      :articleId="comment.article"
      @like-child-comment="likeChildComment"
      @create-child-child-comment="createChildChildComment"
      @update-child-comment="updateChildComment"
      @delete-child-comment="deleteChildComment"
    />
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";

import MainCommentChild from "@/components/articles/MainCommentChild";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MainCommentList",
  components: {
    MainCommentChild,
  },
  props: {
    comment: Object,
    articleId: Number,
  },
  data() {
    return {
      childDiv: false,
      childComment: null,
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
          // console.log(response)
          this.$emit("like-comment", commentId, response.data);
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
        url: `${API_URL}/articles/${this.articleId}/comment_create/${this.comment.id}/comment_create/`,
        headers: {
          Authorization: `Token ${this.token}`,
        },
        data: {
          content: this.childComment,
        },
      })
        .then((response) => {
          // console.log(response);
          this.$emit("create-child-comment", this.comment.id, response.data);
        })
        .catch((error) => {
          console.log(error);
        });

      this.childComment = null;
      this.childDiv = false;
    },
    likeChildComment(childCommentId, childCommentData) {
      const newComment = this.comment.child_comment.map((child) => {
        if (child.id === childCommentId) {
          return childCommentData;
        } else {
          return child;
        }
      });
      this.$emit("like-child-comment", this.comment.id, newComment);
    },
    createChildChildComment(childChildComment) {
      const newComment = this.comment.child_comment
      newComment.push(childChildComment);
      this.$emit("create-child-child-comment", this.comment.id, newComment);
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
        url: `${API_URL}/articles/${this.articleId}/comment/${this.comment.id}/`,
        headers: {
          Authorization: `Token ${this.token}`,
        },
        data: {
          content: this.updateCommentData,
        },
      })
      .then((response) => {
        // console.log(response);
        this.$emit("update-comment", this.comment.id, response.data);
        this.updateOnToggle();
      })
      .catch((error) => {
        console.log(error);
      });
    },
    deleteComment() {
      axios({
        method: "DELETE",
        url: `${API_URL}/articles/${this.articleId}/comment/${this.comment.id}/`,
        headers: {
          Authorization: `Token ${this.token}`,
        },
        data: {
          content: this.updateCommentData,
        },
      })
      .then(() => {
        // console.log(response);
        this.$emit("delete-comment", this.comment.id);
      })
      .catch((error) => {
        console.log(error);
      });
    },
    updateChildComment(commentId, commentData) {
      const newComment = this.comment.child_comment.map((child) => {
        if (child.id === commentId) {
          return commentData;
        } else {
          return child;
        }
      });
      this.$emit("like-child-comment", this.comment.id, newComment);
    },
    deleteChildComment(commentId) {
      const newComment = this.comment.child_comment.filter((child) => {
        return child.id !== commentId;
      })
      this.$emit("delete-child-comment", this.comment.id, newComment, commentId);
    },
  },
};
</script>

<style>
</style>