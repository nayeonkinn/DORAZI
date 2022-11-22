<template>
  <div>
    <router-link :to="{ name: 'ProfileView', params: { username: writer } }">
      <h3>{{ writer }}</h3>
    </router-link>
    <h4>{{ content }}</h4>
    <div>{{ updatedate }}</div>
    <div>{{ likenum }}</div>

    <div v-if="userId === article.user.id">
      <b-button variant="light" @click="Delete">삭제하기</b-button>
      <b-button variant="light" id="show-btn" @click="showModal">
        수정하기
      </b-button>
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
  </div>
</template>

<script>
import axios from "axios";
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
      spoiler: this.article.spoiler,
    };
  },
  computed: {
    userId() {
      return this.$store.state.userId;
    },
    writer() {
      return this.article.user.username;
    },
    updatedate() {
      return this.article.updated_at.slice(0, 10);
    },

    likenum() {
      return this.article.like_users.lenght;
    },
    content() {
      return this.article.content;
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
    Delete() {
      axios({
        method: "DELETE",
        url: `${API_URL}/articles/${this.article.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          this.hideModal();
          this.$emit("update");
        })
        .catch((err) => {
          console.log(err);
        });
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
</style>