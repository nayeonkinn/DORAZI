<template>
  <div v-if="!comment.parent_comment">
    <div class="commentBox p-4">
      <div class="d-flex justify-content-between">
        <div class="d-flex">
          <div>
            <span
              @click="goProfile(comment.user.username)"
              class="cursorPointer"
            >
              {{ comment.user.username }}
            </span>
          </div>
          <div
            class="p-1"
            style="margin-left: 5px; font-size: 12px; color: rgb(100, 100, 100)"
          >
            <span>{{ commentCreatedAt(comment) }}</span>
          </div>
        </div>
        <div>
          <span v-if="updateOn">
            <button class="buttons" @click="updateComment">수정</button>
            <button class="buttons" @click="updateOnToggle">취소</button>
          </span>
          <span v-if="comment.user.id === userId">
            <span v-if="!updateOn">
              <button class="buttons" @click="updateOnToggle">수정</button>
            </span>
            <button class="buttons" @click="deleteComment">삭제</button>
          </span>
          <button class="buttons" @click="childDivToggle">답글 달기</button>
          <button
            class="buttons"
            @click="likeComment(comment.article, comment.id)"
          >
            {{ commentMsg(comment) }} {{ comment.like_users.length }}
          </button>
        </div>
      </div>
      <div class="commentText" :class="{ updating: updateOn }">
        <span v-if="!updateOn">{{ comment.content }} </span>
        <span v-else>
          <textarea
            class="commentUpdate"
            rows="1"
            :value="comment.content"
            @input="updateInput"
            @keyup="adjustHeight()"
            @keydown="adjustHeight()"
          ></textarea>
        </span>
      </div>
    </div>

    <div v-if="childDiv" class="childCommentBox">
      <form @submit.prevent="createChildComment">
        <textarea v-model="childComment" class="childCommentText"></textarea>
        <div class="d-flex justify-content-end">
          <button class="buttons">등록</button>
        </div>
      </form>
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
      const newComment = this.comment.child_comment;
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
      if (!this.updateCommentData || !this.updateCommentData.trim()) {
        alert("내용을 입력해주세요.");
        this.updateCommentData = null;
        return;
      }

      axios({
        method: "PUT",
        url: `${API_URL}/articles/${this.articleId}/comment/${this.comment.id}/`,
        headers: {
          Authorization: `Token ${this.token}`,
        },
        data: {
          content: this.updateCommentData.trim(),
        },
      })
        .then((response) => {
          // console.log(response);
          this.$emit("update-comment", this.comment.id, response.data);
          this.updateOnToggle();
          alert("댓글이 수정되었습니다.");
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
          alert("댓글이 삭제되었습니다.");
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
      });
      this.$emit(
        "delete-child-comment",
        this.comment.id,
        newComment,
        commentId
      );
    },
    adjustHeight() {
      const textarea = document.querySelector(".commentUpdate");
      textarea.style.height = "1px";
      textarea.style.height = 12 + textarea.scrollHeight + "px";
    },
  },
};
</script>

<style>
.cursorPointer {
  cursor: pointer;
}

.commentBox {
  background-color: white;
  width: 100%;
  border-top: solid 1px rgb(187, 187, 187);
  text-align: left;
}

.commentText {
  background-color: rgb(241, 241, 241);
  margin-top: 10px;
  padding: 20px;
  border-radius: 5px;
}

.commentUpdate {
  width: 100%;
  border: none;
  resize: none;
  background-color: rgb(187, 187, 187);
  border-radius: 5px;
}

.commentUpdate:focus {
  outline: none;
}

.childCommentBox {
  background-color: white;
  width: 100%;
  padding: 0px 1.5rem 1.5rem 1.5rem;
  text-align: left;
}

.childCommentText {
  width: 100%;
  border: none;
  resize: none;
  background-color: rgb(187, 187, 187);
  border-radius: 5px;
}
</style>