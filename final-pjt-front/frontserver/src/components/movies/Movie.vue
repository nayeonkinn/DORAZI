<template>
<div class="card" style="width: 18rem;">
  <router-link :to="{ name:'MovieDetailView' , params: { 'movie_pk': movie.id }}"> 
    <img :src="poster" class="card-img-top" alt="poster">
  </router-link>  
  <div class="card-body">
    <h5 class="card-title">{{ title }}</h5>
    <p class="card-text">{{ releasedate.slice(0,4)}}</p>
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
    }

}
</script>




<style>

</style>