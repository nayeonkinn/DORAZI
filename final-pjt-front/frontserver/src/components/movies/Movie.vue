<template>
<div class="section" style="width: 18rem;">
  <router-link :to="{ name:'MovieDetailView' , params: { 'movie_pk': movie.id }}"> 
  <figure class="figure">
      <img class='poster' :src="poster"  alt="poster">
      
      <figcaption class="caption">
        {{ title }} <br>
        {{ releasedate.slice(0,4)}}
      </figcaption>
    </figure>
  </router-link>  
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
  @import '@/assets/main.css';

</style>