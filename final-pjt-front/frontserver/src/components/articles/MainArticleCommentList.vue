<template>
  <div v-if="!comment2.parent_comment">
    <span @click="goProfile(comment2.user.username)">
      {{ comment2.user.username }}
    </span
    >- {{ comment2.content }}
    <button @click="likeComment(comment2.article, comment2.id)">
      {{ commentMsg(comment2) }}
    </button>
    <span> {{ comment2.like_users.length }} </span>
    <span> {{ commentCreatedAt(comment2) }} </span>
		
		<div v-for="child in comment2.child_comment" :key="`comment-${child.id}`">
			<p>ㄴ <span @click="goProfile(comment2.user.username)">{{ child.user.username }}</span>
				- <span v-if="child.mention_to">@{{ child.mention_to }} </span>{{ child.content }}
				<button @click="likeComment(comment2.article, child.id)">
					{{ commentMsg(child) }}
				</button>
				<span> {{ child.like_users.length }} </span>
				<span> {{ commentCreatedAt(child) }} </span>

			</p>

		</div>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MainArticleCommentList",
  props: {
    comment: Object,
  },
  data() {
    return {
      comment2: null,
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
					if (!response.data.parent_comment) {
						this.comment2 = response.data;
					} else {
						this.comment2.child_comment = this.comment2.child_comment.map((child) => {
							if (child.id === commentId) {
								return response.data
							} else {
								return child
							}
						})
					}
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
  },
  created() {
    this.comment2 = this.comment;
  },
};
</script>

<style>
</style>