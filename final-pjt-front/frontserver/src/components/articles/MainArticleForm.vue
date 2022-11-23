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
              style="font-size: 20px; font-weight: 600; margin-right: 10px;"
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

          <div class="star-rating2 space-x-4 mx-1">
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
          <form id="contentForm">
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
          </form>
        </form>
      </div>
    </div>
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
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
.star-rating2 {
  display: flex;
  flex-direction: row-reverse;
  font-size: 1.5rem;
  line-height: 2.5rem;
  justify-content: space-around;
  padding: 0 0.2em;
  text-align: center;
  width: 5em;
}

.star-rating2 input {
  display: none;
}

.star-rating2 label {
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1.5px;
  -webkit-text-stroke-color: #2b2a29;
  cursor: pointer;
}

.star-rating2 :checked ~ label {
  -webkit-text-fill-color: gold;
}

.star-rating2 label:hover,
.star-rating2 label:hover ~ label {
  -webkit-text-fill-color: #fff58c;
}

.formBox {
  height: 250px;
  outline: none;
  background: white;
  color: black;
}

#poster {
  cursor: pointer;
  position: relative;
  top: 10px;
  left: 10px;
}

#content {
  margin: 10px;
  margin-left: 20px;
}

.checkbox input {
  display: none;
}

.checkbox_icon {
  display: inline-block;
  width: 20px;
  height: 20px;
  background-color: transparent;
  border: 1px solid rgb(0, 0, 0);
  position: relative;
  top: 3px;
  left: 3px;
  cursor: pointer;
}

.checkbox_icon::before,
.checkbox_icon::after {
  content: "";
  display: inline-block;
  width: 1px;
  height: 0;
  background-color: rgb(0, 0, 0);
  position: absolute;
  transform-origin: left top;
}

.checkbox_icon::before {
  top: 9px;
  left: 2px;
  transform: rotate(-45deg);
}

.checkbox_icon::after {
  top: 16px;
  left: 9px;
  transform: rotate(-135deg);
}

.checkbox input:checked + .checkbox_icon {
  border-color: rgb(0, 0, 0);
}

.checkbox input:checked + .checkbox_icon::before {
  height: 10px;
  transition: all 0.15s ease;
}

.checkbox input:checked + .checkbox_icon::after {
  height: 20px;
  transition: all 0.15s ease 0.15s;
}

.checkbox_text {
  margin-left: 8px;
  font-size: 17px;
  cursor: pointer;
}

#contentInput {
  border: none;
  resize: none;
  background-color: rgb(241, 241, 241);
  border-radius: 10px;
  width: 100%;
  height: 135px;
}

#contentInput:focus {
  outline: none;
}

#contentForm {
  position: relative;
}

#contentBtn {
  position: absolute;
  border: none;
  right: 3px;
  bottom: 10px;
  color: black;
  text-decoration: none;
}
</style>