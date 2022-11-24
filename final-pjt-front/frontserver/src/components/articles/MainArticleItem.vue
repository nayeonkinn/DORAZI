<template>
  <div class="container">
    <div class="articleBox">
      <div
        class="backdropImg d-flex flex-column justify-content-between"
        alt="backdrop_img"
        :style="{
          background: `linear-gradient(
            to bottom,
            rgba(20, 20, 20, 0) 10%,
            rgba(20, 20, 20, 0.5) 25%,
            rgba(20, 20, 20, 0.8) 50%,
            rgba(20, 20, 20, 0.9) 75%,
            rgba(20, 20, 20, 1) 100%
          ),url(${this.backdrop_path})`,
        }"
      >
        <div class="d-flex justify-content-between" style="position: relative">
          <span
            @click="goProfile(article.user.username)"
            style="cursor: pointer"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              fill="currentColor"
              class="bi bi-person-circle mx-2"
              viewBox="0 0 16 16"
              style="
                position: relative;
                bottom: 3px;
                filter: drop-shadow(1px 1px 1px gray);
              "
            >
              <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" />
              <path
                fill-rule="evenodd"
                d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"
              />
            </svg>
            <span
              style="
                font-size: 30px;
                font-weight: 700;
                text-shadow: 1px 1px 1px gray;
              "
              >{{ article.user.username }}</span
            >
          </span>
          <div>
            <div v-if="userId === article.user.id">
              <button id="show-btn" class="buttons" @click="showModal">
                수정
              </button>
              <button class="buttons" @click="deleteArticle">삭제</button>
            </div>
          </div>
        </div>
        <div>
          <div class="d-flex">
            <div>
              <img
                :src="poster_path"
                alt="poster_img"
                style="width: 100px; height: 150px; cursor: pointer"
                @click="tomovie"
              />
            </div>
            <div class="mx-4 mb-1 d-flex flex-column justify-content-end">
              <div class="d-flex align-items-center">
                <span style="font-size: 40px; font-weight: 800">{{
                  movieTitle
                }}</span>
                <span
                  style="
                    font-size: 20px;
                    color: rgb(255, 200, 47);
                    margin-left: 10px;
                  "
                  >★ {{ article.rating }}</span
                >
              </div>
              <span>{{ article_created_at }}</span>
            </div>
          </div>
        </div>
      </div>

      <div class="p-5">
        <p v-if="!spoiler" style="line-height: 170%"><pre style="font-size:1rem;">{{ article.content }}</pre></p>
        <p v-else>
          주의! 스포일러가 포함되어 있습니다.
          <span
            @click="spoilerToggle"
            style="cursor: pointer; color: rgb(148, 148, 148)"
            >내용 확인하기</span
          >
        </p>
      </div>

      <b-modal
        id="modal-lg"
        size="lg"
        ref="my-modal"
        hide-footer
        hide-header-close
        title="게시글 수정"
      >
        <div class="formBox d-flex mb-5">
          <div id="poster" @click="showModal"></div>
          <div id="content" class="p-2" style="width: 100%">
            <form>
              <div class="container d-flex">
                <div class="col-md-4">
                  <p
                    style="
                      font-size: 20px;
                      font-weight: 600;
                      margin-right: 10px;
                    "
                  >
                    {{ movieTitle }}
                  </p>
                </div>
                <div class="col-lg-4 md-auto"></div>
                <div class="col-md-2 mt-3 pb-3" style="white-space: nowrap">
                  <label class="checkbox">
                    <input
                      id="spoiler"
                      type="checkbox"
                      v-model="spoiler"
                      true-value="yes"
                      false-value="no"
                      name="spolier"
                    />
                    <span class="checkbox_icon"></span>
                    <span class="checkbox_text">스포일러</span>
                  </label>
                </div>
                <!-- <div class="col-md-1"></div> -->

                <div class="star-rating2 m-auto col-md-2">
                  <input
                    type="radio"
                    id="5-stars"
                    name="rating"
                    value="5"
                    v-model="ratings"
                  />
                  <label for="5-stars" class="star pr-4">★</label>
                  <input
                    type="radio"
                    id="4-stars"
                    name="rating"
                    value="4"
                    v-model="ratings"
                  />
                  <label for="4-stars" class="star">★</label>
                  <input
                    type="radio"
                    id="3-stars"
                    name="rating"
                    value="3"
                    v-model="ratings"
                  />
                  <label for="3-stars" class="star">★</label>
                  <input
                    type="radio"
                    id="2-stars"
                    name="rating"
                    value="2"
                    v-model="ratings"
                  />
                  <label for="2-stars" class="star">★</label>
                  <input
                    type="radio"
                    id="1-star"
                    name="rating"
                    value="1"
                    v-model="ratings"
                  />
                  <label for="1-star" class="star">★</label>
                </div>
              </div>

              <div id="contentForm">
                <textarea
                  id="contentInput2"
                  class="p-3"
                  v-model="articlecontent"
                  placeholder="후기를 입력해주세요"
                ></textarea>
                <button id="contentBtn" class="btn btn-link" @click.prevent="sending">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="20"
                    height="20"
                    fill="currentColor"
                    class="bi bi-arrow-right"
                    viewBox="0 0 16 16"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"
                    />
                  </svg>
                </button>
              </div>
            </form>
          </div>
        </div>
      </b-modal>
      <div
        style="text-align: left; margin-left: 25px; color: rgb(148, 148, 148)"
      >
        <span
          v-if="likeUsers.length"
          @click="likeDivToggle"
          style="cursor: pointer"
          id="likeUserComment"
        >
          {{ likeUsers[likeUsers.length - 1].username }}님 외
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
          <span @click="commentDivToggle" style="cursor: pointer">
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
    </div>
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
      articlecontent: this.$store.state.articledetail,
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
        "https://image.tmdb.org/t/p/w300/" + this.article.movie.poster_path
      );
    },
    backdrop_path() {
      return (
        "https://image.tmdb.org/t/p/w1280/" + this.article.movie.backdrop_path
      );
    },
    movieTitle() {
      return this.article.movie.title;
    },
    commentCount() {
      return this.comments.length;
    },
  },
  methods: {
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
    tomovie() {
      this.$router.push({
        name: "MovieDetailView",
        params: { movie_pk: this.article.movie.id },
      });
    },
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
          this.$emit("delete-article", this.article.id);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    spoilerToggle() {
      this.spoiler = !this.spoiler;
    },
  },
  created() {
    // console.log(this.article)
    this.setLikeData(this.article);
    this.comments = this.article.articlecomment_set;
    this.spoiler = this.article.spoiler;
  },
};
</script>

<style>
.articleBox {
  outline: none;
  background: white;
  color: black;
  border-radius: 5px;
  /* padding: 10px; */
  margin-bottom: 3rem;
}
.backdropImg {
  height: 300px;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  background-size: cover !important;
  text-align: left;
  color: white;
  padding: 20px;
}
.buttons {
  border: none;
  outline: none;
  margin-left: 8px;
  border-radius: 10px;
  font-size: 15px;
  padding-inline: 7px;
  background-color: white;
}
#likeBtn {
  transition: all 0.2s linear;
}
#likeBtn:hover {
  transform: scale(1.1);
}
.likeColor {
  color: rgb(255, 200, 47);
}
.notLikeColor {
  color: rgb(241, 241, 241);
}
#likeUserName {
  margin-right: 10px;
}
#likeUserName:hover {
  color: rgb(255, 200, 47);
}
#likeUserComment:hover {
  color: rgb(53, 53, 53);
}
</style>