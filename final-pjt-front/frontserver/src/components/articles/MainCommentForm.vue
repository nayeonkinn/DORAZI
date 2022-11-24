<template>
  <div
    class="p-4"
    style="border-top: solid 1px rgb(187, 187, 187); text-align: left"
  >
    <div class="d-flex justify-content-between">
      <span>{{ username }}</span>
      <button type="submit" form="createForm" class="buttons">등록</button>
    </div>
    <div class="commentText">
      <form id="createForm" @submit.prevent="createComment">
        <textarea
          v-model="comment"
          class="commentUpdate"
          style="background-color: rgb(241, 241, 241)"
          @keyup="adjustHeight()"
          @keydown="adjustHeight()"
        ></textarea>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MainCommentForm",
  props: {
    articleId: Number,
  },
  data() {
    return {
      comment: null,
    };
  },
  computed: {
    token() {
      return this.$store.state.token;
    },
    username() {
      return this.$store.state.username;
    },
  },
  methods: {
    createComment() {
      axios({
        method: "POST",
        url: `${API_URL}/articles/${this.articleId}/comment_create/`,
        headers: {
          Authorization: `Token ${this.token}`,
        },
        data: {
          content: this.comment,
        },
      })
        .then((response) => {
          // console.log(response)
          this.$emit("create-comment", response.data);
					alert('댓글이 작성되었습니다.')
        })
        .catch((error) => {
          console.log(error);
        });

      this.comment = null;
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
</style>