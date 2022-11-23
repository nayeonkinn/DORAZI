<template>
  <div>
    <div
      id="header"
      :style="{background: `linear-gradient(
            to left,
            rgba(20, 20, 20, 0) 10%,
            rgba(20, 20, 20, 0.25) 25%,
            rgba(20, 20, 20, 0.5) 50%,
            rgba(20, 20, 20, 0.75) 75%,
            rgba(20, 20, 20, 1) 100%
          ),url(https://image.tmdb.org/t/p/original/${this.backdrop}) center fixed`,
      }"
    >
      <div class="container">
        <div class="row align-items-center">
          <div class="col-md-8">
            <div class="header-content">
              <h2>{{ movietitle }}</h2>
              <p>{{ movieinfo.original_title }}</p>
              <div id="contact">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-6">
                      <div class="contact-info">
                        <h2>{{ movieinfo.vote_average }}</h2>
                        <p>
                          {{ movieinfo.genre_ids }}
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <b-button variant="light" @click="wishtoggle">
                {{ wishMsg }}
              </b-button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="row align-items-center text-start">
        <div class="col-md-3">
          <img :src="poster" alt="poster" />
        </div>
        <div class="product col-md-6">
          <h3>{{ movietitle }}</h3>
          <p class="desc">{{ overview }}</p>
        </div>
      </div>
    </div>
    <b-button class="button"> 더보기 </b-button>
    <div>
      <b-button variant="light" id="show-btn" @click="showModal"
        >게시글 작성</b-button>

      <b-modal ref="my-modal" hide-footer title="Using Component Methods">
        <div class="d-block text-center">
          <h3>게시글 작성</h3>
          <form @submit.prevent="createArticle">
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
              @click="createArticle"
            >
              작성
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
    <!-- <div>
      <h3>게시글 작성</h3>
      <form @submit.prevent="createArticle">
        <label for="content">내용 : </label>
        <textarea
          id="content"
          cols="30"
          rows="10"
          v-model="articlecontent"
        ></textarea
        ><br />
        <input type="submit" id="submit" />
      </form>
    </div> -->
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
          console.log(this.movieinfo);
          const wishUsers = this.movieinfo.wish_users;
          this.poster = `https://image.tmdb.org/t/p/w185/${res.data.poster_path}`;
          this.backdrop = this.movieinfo.backdrop_path;
          this.movietitle = this.movieinfo.title;
          this.overview = this.movieinfo.overview;
          this.release_date = this.movieinfo.release_date.slice(0, 4);
          this.articlelist = this.movieinfo.articles_list;
          this.iswished = wishUsers.some((user) => user.id === this.userId);
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
.button {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  background-color: transparent;
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
