<template>
  <div>
    <h1>MovieView</h1>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/movies/MovieList.vue';

export default {
  name:"MovieView",
  components:{
    MovieList,

  }
}
</script>

<style>

</style>