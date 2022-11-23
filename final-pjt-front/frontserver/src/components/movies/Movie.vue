<template>
<div class="movie-card" @click="todetail">
    <div class="card-head1">
      <img class='card-img' :src="poster"  alt="poster">
    </div>  
    <div class="card-body">
      <h3 class="card-title1">{{ title }}</h3>

      <div class="card-info">
        <span class="genre"> {{ genres }} </span>
        <span class="year">{{ releasedate }}</span>
      </div>
    </div>
</div>
</template>

<script>
import moment from 'moment';
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
    name:'SingleMovie',
    props:{
      movie:Object
    },
    data(){
      return {
        moviedetail: {},
        title: this.movie.title,
        poster: `https://image.tmdb.org/t/p/w185/${this.movie.poster_path}`,
        // releasedate: this.movie.release_date,
        genres : null,
        releasedate: null,
      }
    },
    computed: {

      },
    methods: {
      todetail(){
        this.$router.push({ name:'MovieDetailView' , params: { 'movie_pk': this.movie.id }})
      },
      detaildata() {
      const movie_pk = this.movie.id;
      axios({
        method: "get",
        url: `${API_URL}/movies/${movie_pk}/`,
        data: {},
      })
        .then((res) => {
          this.moviedetail = res.data;
          console.log(this.moviedetail);
          const genre_ids = this.moviedetail.genre_ids.split(' ')
          if (genre_ids[1]) {
            this.genres = genre_ids[0] + '/' + genre_ids[1]
          }
          else {
            this.genres =  genre_ids[0]
          }
          this.releasedate = moment(String(this.moviedetail.release_date)).format("YYYY")
        })
      }

    },
    created(){
      this.detaildata()
    }

}
</script>




<style>
  @import '@/assets/main.css';
</style>