<template>
<div class="movie-card" @click="todetail">
    <div class="card-head1">
      <img class='card-img' :src="poster"  alt="poster">
    </div>  
    <div class="card-body">
      <h3 class="card-title1">{{ title }}</h3>

      <div class="card-info">
        <span class="genre"> Action/Comedy </span>
        <span class="year">{{ releasedate.slice(0,4)}}</span>
      </div>
    </div>
</div>
</template>

<script>

export default {
    name:'SingleMovie',
    props:{
      movie:Object
    },
    data(){
      return {
        title: this.movie.title,
        poster: `https://image.tmdb.org/t/p/w185/${this.movie.poster_path}`,
        releasedate: this.movie.release_date,
      }
    },
    methods: {
      todetail(){
        this.$router.push({ name:'MovieDetailView' , params: { 'movie_pk': this.movie.id }})
      }

    }

}
</script>




<style>
  @import '@/assets/main.css';
</style>