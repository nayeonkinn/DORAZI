<template>
  <div>
    <div
      class="single"
      :style="{
        'background-image': `url(https://image.tmdb.org/t/p/original/${this.backdrop})`,
      }"
    ></div>
    <img :src="poster" class="poster" alt="poster" />
    <div>{{ title }}</div>
    <div>{{ movieinfo.release_date.slice(0,4)}}</div>
    <div>{{ overview }}</div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MovieDetail",
  data() {
    return {
      movieinfo: null,
      poster: null,
      backdrop: null,
      title: null,
      overview : null,

    };
  },
  created() {
    const movie_pk = this.$route.params.movie_pk;
    axios({
      method: "get",
      url: `${API_URL}/movies/${movie_pk}/`,
      data: {},
    })
      .then((res) => {
        console.log(res);
        this.movieinfo = res.data;
        this.poster = `https://image.tmdb.org/t/p/w185/${res.data.poster_path}`;
        this.backdrop = this.movieinfo.backdrop_path;
        this.title = this.movieinfo.title;
        this.overview = this.movieinfo.overview;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style>
.poster {
  width: 15%;
  height: 15%;
}
</style>