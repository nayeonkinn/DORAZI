<template>
  <div class="commentBox p-4" style="padding-left: 60px !important">
    <div class="d-flex justify-content-between">
      <div class="d-flex">
        <div>
          <span @click="goProfile(child.user.username)" class="cursorPointer">
            {{ child.user.username }}
          </span>
        </div>
        <div
          class="p-1"
          style="margin-left: 5px; font-size: 12px; color: rgb(100, 100, 100)"
        >
          <span>{{ commentCreatedAt(child) }}</span>
        </div>
      </div>
      <div>
        <span v-if="updateOn">
          <button class="buttons" @click="updateComment">수정</button>
          <button class="buttons" @click="updateOnToggle">취소</button>
        </span>
        <span v-if="child.user.id === userId">
          <span v-if="!updateOn">
            <button class="buttons" @click="updateOnToggle">수정</button>
          </span>
          <button class="buttons" @click="deleteComment">삭제</button>
        </span>
        <button class="buttons" @click="childChildDivToggle">답글 달기</button>
        <button class="buttons" @click="likeComment(articleId, child.id)">
          {{ commentMsg(child) }} {{ child.like_users.length }}
        </button>
      </div>
    </div>

    <div class="commentText" :class="{'updating' : updateOn}">
      <span v-if="!updateOn"
        ><span
          v-if="child.mention_to"
          @click="goProfile(child.user.username)"
          class="cursorPointer"
          style="color: rgb(100, 100, 100); margin-right: 5px"
          >@{{ child.mention_to }} </span
        >{{ child.content }}
      </span>
      <span v-else>
        <textarea
          class="commentUpdate"
          rows="1"
          :value="child.content"
          @input="updateInput"
          @keyup="adjustHeight()"
          @keydown="adjustHeight()"
        ></textarea>
      </span>
    </div>

    <div v-if="childChildDiv" class="childCommentBox paddingChildChild">
      <form @submit.prevent="createChildChildComment">
        <textarea v-model="childChildComment" class="childCommentText"></textarea>
        <div class="d-flex justify-content-end">
          <button class="buttons">등록</button>
        </div>
      </form>
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
      if (!this.updateCommentData || !this.updateCommentData.trim()) {
        alert("내용을 입력해주세요.");
        this.updateCommentData = null;
        return;
      }
      axios({
        method: "PUT",
        url: `${API_URL}/articles/${this.articleId}/comment/${this.child.id}/`,
        headers: {
          Authorization: `Token ${this.token}`,
        },
        data: {
          content: this.updateCommentData.trim(),
        },
      })
        .then((response) => {
          // console.log(response);
          this.$emit("update-child-comment", this.child.id, response.data);
          this.updateOnToggle();
          alert('댓글이 수정되었습니다.')
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
          alert('댓글이 삭제되었습니다.')
        })
        .catch((error) => {
          console.log(error);
        });
    },
    adjustHeight() {
      const textarea = document.querySelector('.commentUpdate')
      textarea.style.height = "1px";
      textarea.style.height = 12 + textarea.scrollHeight + "px";
    },
  },
  created() {
    this.child2 = this.child;
  },
};
</script>

<style>

.updating {
  background-color: rgb(187, 187, 187) !important;
}

.paddingChildChild {
  padding: 1.5rem 0px 0px 0px !important;
}

</style>