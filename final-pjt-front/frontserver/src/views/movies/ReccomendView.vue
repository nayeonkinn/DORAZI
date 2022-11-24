<template>
  <div>
    <!-- 영화 배너 -->
    <div class="my-5">
      <h1>오늘의 추천 영화는 이거예요</h1>
    </div>
    <Moviebanner v-if="titlemovie" :movie="titlemovie" />
    <br><br>

    <!-- 영화 리스트 -->
    <div class="container container3">
      <section class="movies">
        <div class="text-start my-5">
          <h2>저번에 찾아본 이 영화는 어때요?</h2>
        </div>
        <div class="movies-grid">
          <Movie
            v-for="movie in recommendlist"
            :key="movie.id"
            :movie="movie"
          />
        </div>
        <hr />
        <div class="text-start my-5">
          <h2>친구들이 후기를 남긴 이 영화는 어때요?</h2>
        </div>
        <div class="movies-grid">
          <Movie
            v-for="movie in friendrecommendlist"
            :key="movie.id"
            :movie="movie"
          />
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import Movie from "@/components/movies/Movie.vue";
import Moviebanner from "@/components/movies/Moviebanner";
import axios from "axios";
import _ from "lodash";
import moment from "moment";

const APIURL = "http://127.0.0.1:8000";
export default {
  name: "MovieView",
  components: {
    Movie,
    Moviebanner,
  },
  data() {
    return {
      recommendlist: [],
      friendrecommendlist: [],
      username: this.$store.state.username,
      titlemovie: false,
      url: null,
      genres: null,
      recommend: [],
      limit: -14,
    };
  },
  computed: {
    randommovie() {
      // const friend = _.sample(this.friendrecommendlist)
      const search = _.sample(this.recommendlist);
      return search;
    },
    releasedate() {
      return moment(String(this.titlemovie.release_date)).format("YYYY");
    },
  },

  methods: {
    todetail() {
      this.$router.push({
        name: "MovieDetailView",
        params: { movie_pk: this.titlemovie.id },
      });
    },
    makelist() {
      axios({
        method: "GET",
        url: `${APIURL}/profile/${this.username}/recommend/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          // console.log(res.data);
          // this.recommendlist = res.data
          const recommend = res.data;
          this.recommendlist = this.limit
            ? recommend.slice(this.limit)
            : recommend;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    friendlist() {
      axios({
        method: "get",
        url: `${APIURL}/profile/${this.username}/recommend_friend/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          // console.log(res);
          // this.friendrecommendlist = res.data
          const recommendlist = res.data;
          this.friendrecommendlist = this.limit
            ? recommendlist.slice(this.limit)
            : recommendlist;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    changtitle() {
      axios({
        method: "GET",
        url: `${APIURL}/movies/${this.randommovie.id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          // console.log(res.data);
          this.titlemovie = res.data;
          const back = this.titlemovie.backdrop_path;
          this.url = `https://image.tmdb.org/t/p/original/${back}`;
          const genre_ids = this.titlemovie.genre_ids.split(" ");
          if (genre_ids[1]) {
            this.genres = genre_ids[0] + "/" + genre_ids[1];
          } else {
            this.genres = genre_ids[0];
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  watch: {
    randommovie() {
      this.changtitle();
    },
  },
  created() {
    this.makelist();
    this.friendlist();
  },
};
</script>

<style>
@import "@/assets/main.css";
</style>