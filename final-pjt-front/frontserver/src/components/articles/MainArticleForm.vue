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
              <img :src="posterPath(movie.poster_path)" style="width: 20px; height: 30px;"/>
              <p>{{ movie.title }}</p>
            </span>
          </div>
        </div>
        <div v-else>검색 결과가 없습니다.</div>
      </div>
    </b-modal>
    <img v-if="selectedMoviePath" :src="selectedMoviePath" style="width: 200px; height: 300px;">
    <p v-if="selectedMovieTitle">{{ selectedMovieTitle }}</p>
    <form>
      <textarea cols="50" rows="2"></textarea>
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
    };
  },
  methods: {
    showModal() {
      this.$refs["my-modal"].show();
    },
    hideModal() {
      this.$refs["my-modal"].hide();
      this.result = null
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
      this.keyword = null
    },
    posterPath(path) {
      return "https://image.tmdb.org/t/p/original/" + path;
    },
    selectMovie(movie) {
      this.selectedMovieId = movie.id
      this.selectedMovieTitle = movie.title
      this.selectedMoviePath = this.posterPath(movie.poster_path)
      this.hideModal()
    }
  },
};
</script>

<style>
</style>