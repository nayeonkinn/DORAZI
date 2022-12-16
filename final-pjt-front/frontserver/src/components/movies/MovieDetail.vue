<template>
  <div>
    <Moviebanner v-if="movieinfo" :movie='movieinfo'/>

    <div class="container">
      <div class="row align-items-start text-start my-5 mx-2">
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
    <div>


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

              <div class="star-rating space-x-4 m-auto col-md-2">
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
  <button id="recoBtn" class="buttons" variant="light" @click="showModal">게시물 작성</button>

    <Carousel :per-page="1" class="banner_list" paginationColor="#999" :paginationPadding=3 :perPage='pagelim' :navigationEnabled=true>
      <Slide v-for="article in articlelist.slice().reverse()" :key="article.id" style="width:300px">
        <ArticleList
          :article="article"
          @update="detaildata"
          class="m-2"
        />
      </Slide>
    </Carousel>
  </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
import ArticleList from "@/components/articles/ArticleList";
import Moviebanner from "@/components/movies/Moviebanner";
import { Carousel, Slide } from 'vue-carousel';
export default {
  name: "MovieDetail",
  components: {
    ArticleList,
    Moviebanner,
    Slide,
    Carousel,
  },
  data() {
    return {
      enabled:true,
      pagelim: 5,
      movieinfo: false,
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
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
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
            this.ourrating = this.movieinfo.our_ratings.toFixed(1);
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
          this.$router.push('/404')
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
</style>