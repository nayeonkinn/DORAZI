<template>
  <div>
    <div
      id="header"
      :style="{
            background: `linear-gradient(
            to left,
            rgba(20, 20, 20, 0) 10%,
            rgba(20, 20, 20, 0.25) 25%,
            rgba(20, 20, 20, 0.5) 50%,
            rgba(20, 20, 20, 0.75) 75%,
            rgba(20, 20, 20, 1) 100%
          ),url(https://image.tmdb.org/t/p/original/${this.backdrop}) center fixed no-repeat`,
      }"
    >
      <div class="container">
        <div class="row align-items-center">
          <div class="col-md-6">
            <div class="header-content">
              <h2>{{ movietitle }}</h2>
              <hr />
              <p>{{ originaltitle }}</p>
              <div id="contact">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-6">
                      <div class="contact-info">
                        <h2>평점 : {{ voteaverage }}</h2>
                        <p>장르 : {{ genres }}</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <span style="cursor: pointer" @click="wishtoggle">
                <svg
              id="likeBtn"
              xmlns="http://www.w3.org/2000/svg"
              width="30"
              height="30"
              fill="currentColor"
              class="bi bi-heart-fill"
              viewBox="0 0 16 16"
              :class="[iswished  ? 'likeColor' : 'notLikeColor']"
            >
              <path
                fill-rule="evenodd"
                d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"
              />
            </svg>
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="row align-items-start text-start">
        <div class="col-md-3 my-3 mx-1">
          <img :src="poster" alt="poster" style="border: 3px solid white" />
        </div>
        <div class="product col-md-8 mt-5">
          <div class="col">
            <h3>{{ movietitle }}</h3>
            <h5>유저 평점 : {{ ourrating }}</h5>
            <hr/>
          </div>
          <div>
            <p class="desc">{{ overview }}</p>
          </div>
        </div>
      </div>
    </div>
    <!-- <b-button class="button"> 더보기 </b-button> -->
    <div>
      <button class="buttons" variant="light" id="show-btn" @click="showModal"
        >게시글 작성</button
      >

      <b-modal id="modal-lg" size="lg" ref="my-modal" hide-footer hide-header-close title="게시글 작성">
        <div class="formBox d-flex mb-5">
          <div id="poster" @click="showModal"></div>
          <div id="content" class="p-2" style="width: 100%">
            <form @submit.prevent="createArticle">
              <div class="container d-flex">
                <div class="col-md-4">
                  <p 
                  style="font-size: 20px; font-weight: 600; margin-right: 10px"
                  >
                  {{ movietitle }}
                </p>
              </div>
              <div class="col-lg-4 md-auto"></div>
              <div class="col-md-2 mt-3 pb-3" style="white-space: nowrap;">
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

              <div class="star-rating2 space-x-4 m-auto col-md-2">
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
      </b-modal>
    </div>
<!-- 게시글 리스트 -->
    <div class="cotainer">
      <ArticleList
        v-for="article in articlelist.slice().reverse()"
        :key="article.id"
        :article="article"
        @update="detaildata"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
import ArticleList from "@/components/articles/ArticleList";

export default {
  name: "MovieDetail",
  components: {
    ArticleList,
  },
  data() {
    return {
      movieinfo: null,
      poster: null,
      backdrop: "?",
      movietitle: null,
      overview: null,
      release_date: null,
      articletitle: null,
      articlecontent: null,
      articlelist: [],
      ratings: 0,
      spoiler: false,
      iswished: null,
      originaltitle: null,
      voteaverage: 0,
      genres: null,
      ourrating: "아직 평가가 없어요",
    };
  },
  computed: {
    wishMsg() {
      return this.iswished ? "♥" : "♡";
    },
    userId() {
      return this.$store.state.userId;
    },
  },
  methods: {
    wishtoggle() {
      axios({
        method: "post",
        url: `${API_URL}/movies/${this.movieinfo.id}/wish/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.iswished = !this.iswished;
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
    createArticle() {
      const content = this.articlecontent;
      if (!content) {
        alert("내용을 입력해주세요");
        return;
      }
      axios({
        method: "POST",
        url: `${API_URL}/articles/create/${this.movieinfo.id}/`,
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
          this.articlecontent = null;
          this.detaildata();
          this.hideModal();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    detaildata() {
      const movie_pk = this.$route.params.movie_pk;
      axios({
        method: "get",
        url: `${API_URL}/movies/${movie_pk}/`,
        data: {},
      })
        .then((res) => {
          this.movieinfo = res.data;
          // console.log(this.movieinfo);
          const wishUsers = this.movieinfo.wish_users;
          this.poster = `https://image.tmdb.org/t/p/w185/${res.data.poster_path}`;
          this.backdrop = this.movieinfo.backdrop_path;
          this.movietitle = this.movieinfo.title;
          this.overview = this.movieinfo.overview;
          this.release_date = this.movieinfo.release_date.slice(0, 4);
          this.articlelist = this.movieinfo.articles_list;
          this.iswished = wishUsers.some((user) => user === this.userId);
          this.originaltitle = this.movieinfo.original_title;
          this.voteaverage = this.movieinfo.vote_average;
          this.genres = this.movieinfo.genre_ids;
          if (this.movieinfo.our_ratings) {
            this.ourrating = this.movieinfo.our_ratings;
          }
        })
        .then(() => {
          axios({
            method: "post",
            url: `${API_URL}/movies/${this.movieinfo.id}/enter/`,
            headers: {
              Authorization: `Token ${this.$store.state.token}`,
            },
          }).catch((err) => {
            console.log(err);
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.detaildata();
  },
  mounted() {
    this.detaildata();
  },
};
</script>

<style >
@import "@/assets/style.css";
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

#contentInput2 {
  border: none;
  resize: none;
  background-color: rgb(241, 241, 241);
  border-radius: 10px;
  width: 99%;
  height: 210px;
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
