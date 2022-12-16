<template>
  <div class="container">
    <div class="formBox d-flex mb-5">
      <div id="poster" @click="showModal">
        <div v-if="!selectedMoviePath" class="posterBox">
          <img
            src="https://t1.daumcdn.net/cfile/tistory/99BACC445A4B25F20B"
            style="width: 160px; height: 230px"
            alt="empty poster"
          />
        </div>
        <div v-else>
          <img
            v-if="selectedMoviePath"
            :src="selectedMoviePath"
            style="width: 160px; height: 230px"
            alt="selected movie poster"
          />
        </div>
      </div>
      <div id="content" class="p-2" style="width: 100%">
        <form @submit.prevent="createArticle">
          <div class="d-flex">
            <p
              v-if="selectedMovieTitle"
              style="font-size: 20px; font-weight: 600; margin-right: 10px"
            >
              {{ selectedMovieTitle }} {{ selectedMovieDate }}
            </p>
            <p
              v-else
              style="font-size: 20px; font-weight: 600; margin-right: 10px"
            >
              영화를 선택해주세요
            </p>
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

          <div class="star-rating space-x-4 mx-1">
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
          <div id="contentForm">
            <textarea
              id="contentInput"
              class="p-3"
              v-model="content"
              placeholder="후기를 입력해주세요"
            ></textarea>
            <button id="contentBtn" class="btn btn-link">
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
    <b-modal ref="my-modal" hide-footer hide-header-close title="영화 검색">
      <div class="d-block">
        <form id="searchForm" class="d-flex" @submit.prevent="searchMovie">
          <button id="searchBtn2" class="btn btn-link" type="submit">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-search"
              viewBox="0 0 16 16"
            >
              <path
                d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"
              />
            </svg>
          </button>
          <input
            id="searchInput2"
            type="text"
            class="form-control"
            style="color: black; background-color: rgb(241, 241, 241)"
            placeholder="영화 제목을 입력해주세요"
            v-model="keyword"
          />
        </form>
      </div>
      <div v-if="result" class="mt-3">
        <p style="color: rgb(158, 158, 158)">검색 결과</p>
        <div v-if="result.length">
          <div v-for="movie in result" :key="`movie-${movie.id}`" class="p-1">
            <div class="d-flex align-items-center mb-2">
              <span @click="selectMovie(movie)" class="cursorPointer">
                <img
                  :src="posterPath(movie.poster_path)"
                  style="width: 20px; height: 30px"
                />
              </span>
              <span
                @click="selectMovie(movie)"
                class="cursorPointer"
                style="margin-left: 8px; font-size: 18px"
                >{{ movie.title }}</span
              >
            </div>
          </div>
        </div>
        <div v-else>검색 결과가 없습니다.</div>
      </div>
    </b-modal>
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
      selectedMovieDate: null,
      selectedMoviePath: null,
      ratings: null,
      spoiler: false,
      content: null,
    };
  },
  computed: {
    token() {
      return this.$store.state.token;
    },
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
      if (!this.keyword || !this.keyword.trim()) {
        alert("검색어를 입력해주세요.");
        this.keyword = null;
        return;
      }
      axios({
        method: "get",
        url: `${API_URL}/movies/search/`,
        params: {
          search: this.keyword,
        },
        headers: {
          Authorization: `Token ${this.token}`,
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
      return "https://image.tmdb.org/t/p/w185/" + path;
    },
    selectMovie(movie) {
      this.selectedMovieId = movie.id;
      this.selectedMovieTitle = movie.title;
      this.selectedMovieDate = movie.release_date.substring(0, 4);
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
          this.$emit("create-article", response.data);
          this.selectedMovieId = null;
          this.selectedMovieTitle = null;
          this.selectedMoviePath = null;
          this.ratings = null;
          this.spoiler = null;
          this.content = null;
          alert("후기가 작성되었습니다.");
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>

</style>