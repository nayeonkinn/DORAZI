<template>
  <div>
    <img
      :src="poster_path"
      alt="poster_img"
      style="width: 200px; height: 300px"
    />
    <h3 @click="goProfile(article.user.username)">
      {{ article.user.username }}
    </h3>
    <p>{{ article_created_at }}</p>
    <p>{{ article.rating }}</p>
    <p>{{ article.content }}</p>
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
      commentDiv: true,
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
  },
  methods: {
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
    this.article = this.$store.state.detailarticle
    this.setLikeData(this.article);
    this.comments = this.article.articlecomment_set;
  },
  watch: {
    '$store.state.detailarticle': function() {
      this.article = this.$store.state.detailarticle
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