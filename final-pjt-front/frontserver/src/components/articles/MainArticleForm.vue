<template>
  <div>
    <button @click="showModal">Select Movie</button><br />
    <b-modal ref="my-modal" hide-footer title="Search Movie">
      <div class="d-block text-center">
        <form @submit.prevent="searchMovie">
          <label for="search">영화 제목 </label>
          <input id="search" v-model="keyword" />
          <button>검색</button><br />
        </form>
      </div>
      <div v-if="result">
        <p>검색 결과</p>
        <div v-if="result.length">
          <div v-for="movie in result" :key="`movie-${movie.id}`">
            <span @click="selectMovie(movie)">
              <img
                :src="posterPath(movie.poster_path)"
                style="width: 20px; height: 30px"
              />
              <p>{{ movie.title }}</p>
            </span>
          </div>
        </div>
        <div v-else>검색 결과가 없습니다.</div>
      </div>
    </b-modal>
    <img
      v-if="selectedMoviePath"
      :src="selectedMoviePath"
      style="width: 200px; height: 300px"
    />
    <p v-if="selectedMovieTitle">{{ selectedMovieTitle }}</p>
    <form @submit.prevent="createArticle">
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
      <label for="spoiler"> 스포일러 </label>
      <input
        type="checkbox"
        v-model="spoiler"
        true-value="yes"
        false-value="no"
        name="spolier"
      /> <br>
      <textarea v-model="content" cols="50" rows="2"></textarea> <br>
      <button>작성</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MainArticleForm",
  data() {
    return {
      modalOn: false,
      keyword: null,
      result: null,
      selectedMovieId: null,
      selectedMovieTitle: null,
      selectedMoviePath: null,
      ratings: null,
      spoiler: false,
      content: null,
    };
  },
  computed: {
    token() {
      return this.$store.state.token
    }
  },
  methods: {
    showModal() {
      this.$refs["my-modal"].show();
    },
    hideModal() {
      this.$refs["my-modal"].hide();
      this.result = null;
    },
    searchMovie() {
      axios({
        method: "get",
        url: `${API_URL}/movies/search/`,
        params: {
          search: this.keyword,
        },
      })
        .then((response) => {
          // console.log(response);
          this.result = response.data;
        })
        .catch((err) => {
          console.log(err);
        });
      this.keyword = null;
    },
    posterPath(path) {
      return "https://image.tmdb.org/t/p/original/" + path;
    },
    selectMovie(movie) {
      this.selectedMovieId = movie.id;
      this.selectedMovieTitle = movie.title;
      this.selectedMoviePath = this.posterPath(movie.poster_path);
      this.hideModal();
    },
    createArticle() {
      if (!this.selectedMovieId) {
        alert("영화를 선택해주세요.");
        return;
      } else if (!this.ratings) {
        alert("별점을 입력해주세요.");
        return;
      } else if (!this.content) {
        alert("내용을 입력해주세요.");
        return;
      }
      axios({
        method: "POST",
        url: `${API_URL}/articles/create/${this.selectedMovieId}/`,
        data: {
          content: this.content,
          spoiler: this.spoiler,
          rating: this.ratings,
        },
        headers: {
          Authorization: `Token ${this.token}`,
        },
      })
        .then((response) => {
          // console.log(response);
          this.$emit('create-article', response.data)
          this.selectedMovieId = null
          this.selectedMovieTitle = null
          this.selectedMoviePath = null
          this.ratings = null
          this.spoiler = null
          this.content = null
        })
        .catch((err) => {
          console.log(err);
        });
    }
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