<template>
  <div>
    <section class="movies">
      <h1>MovieView</h1>
      <div class="movies-grid">
        <Movie v-for="movie in movielist" :key="movie.id" :movie="movie"/>
      </div>
      <button class="load-more">LOAD MORE</button>
    </section>
  </div>
</template>

<script>
import Movie from "@/components/movies/Movie.vue";
import axios from "axios";

const API_URL = 'http://127.0.0.1:8000'
export default {
  name:"MovieView",
  components:{
    Movie,

  },
  data() {
    return {
      movielist: []
    };
  },
  computed: {

  },
  methods: {
    makelist() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
        data: {

        }
      })
      .then((res) => {
        // console.log(res);
        this.movielist = res.data
      })
      .catch((err) =>{
        console.log(err);
      })
    }
  },
  mounted(){
    this.makelist()
  }
}
</script>

<style>
  @import '@/assets/main.css';

</style>