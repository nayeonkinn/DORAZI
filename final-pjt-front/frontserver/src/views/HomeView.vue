<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <MovieList/>
  </div>
</template>

<script>
// @ is an alias to /src
import MovieList from '@/components/movies/MovieList.vue'


export default {
  name: 'HomeView',
  components: {
    MovieList
  }
}
</script>
