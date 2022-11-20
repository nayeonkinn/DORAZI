<template>
  <div>
    <h1>Search</h1>
    <div>User</div>
    <div>
        <Movie v-for="movie in movielist" :key="movie.id" :movie="movie"/>
    </div>
  </div>
</template>

<script>
import Movie from "@/components/movies/Movie";

import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "SearchView",
  components: {
    Movie,
  },
  data() {
    return {
      movielist: {},
    };
  },
  methods: {
    makelist() {
        console.log(this.$router)
      axios({
        method: "get",
        url: `${API_URL}/movies/search/`,
        params: {'search': this.$router.params.q},
      })
        .then((res) => {
          console.log(res);
          this.movielist = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  mounted() {
    this.makelist();
  },
};
</script>

<style>
</style>