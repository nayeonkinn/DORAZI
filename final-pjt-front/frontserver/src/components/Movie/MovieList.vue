<template>
  <div class="text-start">
      <Movie v-for="movie in movielist" :key="movie.id" :movie="movie"/>
  </div>
</template>

<script>
import Movie from "@/components/Movie/Movie.vue";
import axios from "axios";

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "MoviesList",
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
        console.log(res);
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
};
</script>

<style>
</style>