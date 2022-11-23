<template>
  <div>
    <img
      :src="poster_path"
      alt="poster_img"
      style="width: 200px; height: 300px"
      @click="tomovie"
    />
    <h3 @click="goProfile(article.user.username)">
      {{ article.user.username }}
    </h3>
    <p>{{ article_created_at }}</p>
    <p>{{ article.rating }}</p>

    <p v-if="!spoiler">{{ article.content }}</p>
    <p v-else>
      주의! 스포일러가 포함되어 있습니다.
      <span @click="spoilerToggle">내용 확인하기</span>
    </p>
    <div v-if="userId === article.user.id">
      <b-button id="show-btn" @click="showModal"> 수정하기 </b-button>
      <button @click="deleteArticle">삭제</button>
      </div>

      <b-modal ref="my-modal" hide-footer title="게시물 수정">
        <div class="d-block text-center">
          <h3>게시글 수정</h3>
          <form @submit.prevent="sending">
            <label for="content">내용 : </label>
            <textarea
              id="content"
              cols="30"
              rows="10"
              v-model="articlecontent"
            ></textarea>
            <!-- 별점 -->
            <!-- https://melthleeth.tistory.com/entry/HTML-CSS%EB%A1%9C-%EB%B3%84%EC%B0%8D%EA%B8%B0-Star-Rating -->
            <div class="star-rating space-x-4 mx-auto">
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
            <!-- 스포일러 여부 -->
            <label for="spoiler"> 스포일러 여부 </label>
            <input
              type="checkbox"
              v-model="spoiler"
              true-value="yes"
              false-value="no"
              name="spolier"
            />

            <br />

            <b-button
              class="mt-3"
              variant="outline-success"
              block
              @click="sending"
            >
              수정
            </b-button>
            <b-button
              class="mt-3"
              variant="outline-danger"
              block
              @click="hideModal"
            >
              취소
            </b-button>
          </form>
        </div>
      </b-modal>


    <button @click="like">{{ likeMsg }}</button>
    <button @click="likeDivToggle">좋아요 {{ likeCount }}</button>
    <button @click="commentDivToggle">댓글 {{ commentCount }}</button>

    <div v-if="likeDiv">
      <div v-for="user in likeUsers" :key="`user-${user.id}`">
        <p @click="goProfile(user.username)">{{ user.username }}</p>
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
    <hr />
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
        "https://image.tmdb.org/t/p/original/" + this.article.movie.poster_path
      );
    },
    likeMsg() {
      return this.isLiked ? "♥" : "♡";
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
      console.log(content);
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
        .then((res) => {
          console.log(res);
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
</style>