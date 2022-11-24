<template>
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
          ),url(https://image.tmdb.org/t/p/original/${this.backdrop}) center no-repeat`,
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
                        <p style="white-space: nowrap;">장르 : {{ genres }}</p>
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
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
export default {
  name:'MovieBanner',
  props: {
    movie:Object,
  },
  data(){
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
      iswished: null,
      originaltitle: null,
      voteaverage: 0,
      genres: null,
      ourrating: "아직 평가가 없어요",
    }
  },
  computed: {
    wishMsg() {
      return this.iswished ? "♥" : "♡";
    },
    userId() {
      return this.$store.state.userId;
    },
  },
  methods:{
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
    detaildata() {
          this.movieinfo = this.movie
          const wishUsers = this.movieinfo.wish_users;
          this.poster = `https://image.tmdb.org/t/p/w185/${this.movie.poster_path}`;
          this.backdrop = this.movie.backdrop_path;
          this.movietitle = this.movie.title;
          this.overview = this.movie.overview;
          this.release_date = this.movie.release_date.slice(0, 4);
          this.articlelist = this.movieinfo.articles_list;
          this.iswished = wishUsers.some((user) => user === this.userId);
          this.originaltitle = this.movieinfo.original_title;
          this.voteaverage = this.movieinfo.vote_average;
          this.genres = this.movieinfo.genre_ids;
          if (this.movieinfo.our_ratings) {
            this.ourrating = this.movieinfo.our_ratings;
          }
    },
  },
  mounted() {
    this.detaildata();
  },
}
</script>

<style>

</style>