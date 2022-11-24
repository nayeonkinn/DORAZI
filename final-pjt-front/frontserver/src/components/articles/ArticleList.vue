<template>
  <div class="container">
    <div class="articleBox" @click="todetail">
      <div class="articlecontent2 p-5">
        <p
          v-if="!spoiler"

        >
          {{ article.content }}
        </p>
        <p v-else>
          주의! 스포일러가 포함되어 있습니다.
          <span
            @click="spoilerToggle"
            style="cursor: pointer; color: rgb(148, 148, 148)"
            >내용 확인하기</span
          >
        </p>
      </div>

      <div
        style="text-align: left; margin-left: 25px; color: rgb(148, 148, 148)"
      >
        <span
          v-if="likeUsers"
          @click="likeDivToggle"
          style="cursor: pointer"
          id="likeUserComment"
        >
          {{ likeUsers[likeCount.length - 1].username }}님 외
          {{ likeCount - 1 }}명이 이 글을 좋아합니다.
        </span>
        <div v-if="likeDiv" class="my-1">
          <span v-for="user in likeUsers" :key="`user-${user.id}`">
            <span
              id="likeUserName"
              @click="goProfile(user.username)"
              style="cursor: pointer"
              >{{ user.username }}</span
            >
          </span>
        </div>
      </div>
      <div class="d-flex p-4">
        <div>
          <span @click="like" style="cursor: pointer">
            <svg
              id="likeBtn"
              xmlns="http://www.w3.org/2000/svg"
              width="30"
              height="30"
              fill="currentColor"
              class="bi bi-heart-fill"
              viewBox="0 0 16 16"
              :class="[isLiked ? 'likeColor' : 'notLikeColor']"
            >
              <path
                fill-rule="evenodd"
                d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"
              />
            </svg>
            <span style="cursor: pointer; margin-left: 10px; font-size: 17px">{{
              likeCount
            }}</span>
          </span>
        </div>
        <div class="mx-4">
          <span @click="commentDivToggle">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="27"
              height="27"
              fill="currentColor"
              class="bi bi-chat-left-fill notLikeColor"
              id="likeBtn"
              viewBox="0 0 16 16"
            >
              <path
                d="M2 0a2 2 0 0 0-2 2v12.793a.5.5 0 0 0 .854.353l2.853-2.853A1 1 0 0 1 4.414 12H14a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"
              />
            </svg>
            <span style="cursor: pointer; margin-left: 10px; font-size: 17px">{{
              commentCount
            }}</span>
          </span>
        </div>
        <div>
          <span @click="toprofile">
            {{ article.user.username }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "ArticleList",
  props: {
    article: Object,
  },
  data() {
    return {
      articlecontent: this.article.content,
      ratings: this.article.rating,

      isLiked: null,
      likeCount: null,
      likeDiv: false,
      likeUsers: null,
      commentDiv: false,
      comments: null,
      spoiler: null,
    };
  },
  computed: {
    token() {
      // console.log(this.article);
      return this.$store.state.token;
    },
    userId() {
      return this.$store.state.userId;
    },
    article_created_at() {
      return moment(String(this.article.created_at)).format("YYYY-MM-DD HH:mm");
    },

    movieTitle() {
      return this.article.movie.title;
    },
    commentCount() {
      return this.comments ? this.comments.length : 0;
    },
  },
  methods: {
    todetail() {
      this.$store.state.articledetail = this.article;
      this.$router.push({
        name: "ArticleDetailView",
        params: { article_id: this.article.id },
      });
    },
    toprofile() {
      this.$router.push({
        name: "ProfileView",
        params: { username: this.writer },
      });
    },
    getActiveStar(index) {
      this.score = index + 1;
    },
    showModal() {
      this.$refs["my-modal"].show();
    },
    hideModal() {
      this.$refs["my-modal"].hide();
    },
    sending() {
      const content = this.articlecontent;
      if (!content) {
        alert("내용을 입력해주세요");
        return;
      }
      // console.log(content);
      axios({
        method: "PUT",
        url: `${API_URL}/articles/${this.article.id}/`,
        data: {
          content: content,
          spoiler: this.spoiler,
          rating: this.ratings,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          // console.log(res);
          this.hideModal();
          this.$emit("update", this.article);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    Delete() {
      axios({
        method: "DELETE",
        url: `${API_URL}/articles/${this.article.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          // console.log(res);
          this.hideModal();
          this.$emit("update");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    setLikeData(article) {
      const likeUsers = article.like_users;
      this.isLiked = likeUsers.some((user) => user.id === this.userId);
      this.likeCount = likeUsers ? likeUsers.length : 0;
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
  },
};
</script>

<style>
.poster {
  width: 15%;
  height: 15%;
}
.star-rating {
  display: flex;
  flex-direction: row-reverse;
  font-size: 2.25rem;
  line-height: 2.5rem;
  justify-content: space-around;
  padding: 0 0.2em;
  text-align: center;
  width: 5em;
}

.star-rating input {
  display: none;
}

.star-rating label {
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 2.3px;
  -webkit-text-stroke-color: #2b2a29;
  cursor: pointer;
}

.star-rating :checked ~ label {
  -webkit-text-fill-color: gold;
}

.star-rating label:hover,
.star-rating label:hover ~ label {
  -webkit-text-fill-color: #fff58c;
}
.articlecontent2 {
  width: 250px; /* 너비는 변경될수 있습니다. */
  height: 150px;
  line-height: 20px;
  overflow: hidden; /* 내용이 길면 감춤니다 */
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
}
</style>