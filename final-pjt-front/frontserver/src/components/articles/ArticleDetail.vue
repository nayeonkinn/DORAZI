<template>
  <div>
    <img
      :src="poster_path"
      alt="poster_img"
      style="width: 200px; height: 300px"
      @click="goMovie" 
    />
    <h3 @click="goProfile(article.user.username)">
      {{ article.user.username }}
    </h3>
    <p>{{ article_created_at }}</p>
    <p>{{ article.rating }}</p>
    <p>{{ article.content }}</p>
    <!-- 수정 삭제 -->
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
              v-model="content"
            ></textarea>
            <!-- 별점 -->
            <!-- https://melthleeth.tistory.com/entry/HTML-CSS%EB%A1%9C-%EB%B3%84%EC%B0%8D%EA%B8%B0-Star-Rating -->
            <div class="star-rating space-x-4 mx-auto">
              <input
                type="radio"
                id="5-stars"
                name="rating"
                value="5"
                v-model="rating"
              />
              <label for="5-stars" class="star pr-4">★</label>
              <input
                type="radio"
                id="4-stars"
                name="rating"
                value="4"
                v-model="rating"
              />
              <label for="4-stars" class="star">★</label>
              <input
                type="radio"
                id="3-stars"
                name="rating"
                value="3"
                v-model="rating"
              />
              <label for="3-stars" class="star">★</label>
              <input
                type="radio"
                id="2-stars"
                name="rating"
                value="2"
                v-model="rating"
              />
              <label for="2-stars" class="star">★</label>
              <input
                type="radio"
                id="1-star"
                name="rating"
                value="1"
                v-model="rating"
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
      <MainArticleCommentList
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
      <MainArticleCommentForm
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

import MainArticleCommentList from "@/components/articles/MainCommentList";
import MainArticleCommentForm from "@/components/articles/MainCommentForm";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "ArticleDetail",
  components: {
    MainArticleCommentList,
    MainArticleCommentForm,
  },
  // props: {
  //   article: Object,
  // },
  data() {
    return {
      article: this.$store.state.articledetail,
      isLiked: null,
      likeCount: null,
      likeDiv: false,
      likeUsers: null,
      commentDiv: false,
      commentCount: null,
      comments: [],
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
    user() {
      return this.$store.state.user;
    },
    username() {
      return this.user.username;
    },
    rating() {
      return this.article.rating
    },
    spoiler() {
      return this.article.spoiler
    },
    content () {
      return this.article.content
    }
  },
  methods: {
    tomovie() {
      this.$router.push({
        name: "MovieDetailView",
        params: { movie_pk: this.article.movie.id },
      });
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
    getActiveStar(index) {
      this.score = index + 1;
    },
    showModal() {
      this.$refs["my-modal"].show();
    },
    hideModal() {
      this.$refs["my-modal"].hide();
    },
    setLikeData() {
      const likeUsers = this.article.like_users;
      this.isLiked = likeUsers.some((user) => user.id === this.userId);
      this.likeCount = likeUsers.length;
      this.likeUsers = this.article.like_users;
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
          rating: this.rating,
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
      })
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
      this.comments.push(commentData)
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
      })
      this.comments = this.comments.filter((comment) => {
        return comment.id !== childId;
      })

    },
    createChildComment(commentId, commentData) {
      this.comments.forEach((comment) => {
        if (comment.id === commentId) {
          comment.child_comment.push(commentData);
        }
      });
      this.comments.push(commentData)
    },
  },
  created() {
    console.log(this.$store.state.articledetail)
    this.article = this.$store.state.articledetail
    this.setLikeData(this.article);
    this.comments = this.article.articlecomment_set;
  },
  watch: {
    '$store.state.detailarticle': function() {
      this.article = this.$store.state.articledetail
    }
  }
}
</script>


<style lang="scss" scoped>
.comments {
  position: relative;
  width: 638px;
  overflow: hidden;

  .process-move-arrow {
    display: flex;
    position: absolute;
    justify-content: center;
    align-items: center;
    width: 30px;
    height: 30px;
    color: #7b7c82;
    background-color: white;
    font-size: 20px;
    border-radius: 50%;
    box-shadow: 0px 0px 1px 0px;
    cursor: pointer;
    opacity: 0.2;
    transition: all 0.5s ease-in-out;

    &:hover {
      color: black;
      opacity: 0.8;
    }
  }

  .left-arrow {
    left: 10px;
    top: 175px;
    z-index: 10;
  }

  .right-arrow {
    right: 10px;
    top: 175px;
  }

  .title {
    margin: 10px 20px 20px;
  }

  > ul {
    display: flex;
    justify-content: flex-start;
    margin: 14px 0px 30px;
    transition: all 0.8s;

    &::-webkit-scrollbar {
      display: none;
    }

    > li {
      display: flex;
      flex-direction: column;
      padding: 15px;
      margin: 0 10px;
      background-color: #f2f2f2;
      border-radius: 5px;
      opacity: 0.9;

      &:first-child {
        margin-left: 15px;
      }

      > div {
        .comment-title {
          display: flex;
          justify-content: space-between;
          align-items: center;
          width: 265px;

          > h3 {
            font-size: 17px;
            font-weight: 600;
          }

          > span {
            padding: 5px 12px;
            font-size: 15px;
            border: 1px solid #eaeaea;
            border-radius: 15px;
            background-color: #ffff;
          }
        }
        &::after {
          content: '';
          display: block;
          margin-top: 10px;
          border-bottom: 1px solid #e5e5e5;
        }
      }

      .comment {
        display: -webkit-box;
        max-width: 270px;
        height: 9rem;
        margin: 15px 0;
        font-size: 15px;
        line-height: 1.5rem;
        word-wrap: break-word;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 6; /* 라인수 */
        overflow: hidden;
        text-overflow: ellipsis;
      }

      .comment-good {
        .fa-thumbs-up {
          margin-right: 5px;
          color: #787878;
          cursor: pointer;
        }

        .like {
          color: pink;
        }

        &::before {
          content: '';
          display: block;
          margin-bottom: 10px;
          border-bottom: 1px solid #e5e5e5;
        }
      }
    }
  }
  &::after {
    content: '';
    display: block;
    margin: 0 auto;
    width: 598px;
    border-bottom: 1px solid #f0f0f0;
  }
}
</style>