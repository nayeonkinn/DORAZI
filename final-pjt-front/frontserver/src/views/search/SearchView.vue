<template>
  <div>
    <h1>Search</h1>
    <div>User</div>
    <div>{{ this.$router.params }}    </div>
    <div>
        <div>
            <Movie v-for="movie in movielist" :key="movie.id" :movie="movie"/>
        </div>
        <router-link class="" v-for="article in articles" :key="article.id" :to="{ name: 'ArticleDetailView', params: {'article_id': article.id }}" >
            <ArticleSimple :article="article"/>
        </router-link>
    </div>
  </div>
</template>

<script>
import Movie from "@/components/movies/Movie";
import ArticleSimple from '@/components/articles/ArticleSimple'

import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "SearchView",
  components: {
    Movie,
    ArticleSimple,
  },
  data() {
    return {
      movielist: {},
      articles : {},
    };
  },
//   computed:{
//     q : this.$store.state.search
//   },
  methods: {
    makelist() {
      axios({
        method: "get",
        url: `${API_URL}/movies/search/`,
        params: {'search': this.$store.state.search},
      })
        .then((res) => {
          console.log(res);
          this.movielist = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getArticles() {
      axios({
        method: "get",
        url: `${API_URL}/articles/search/`,
        params: {'search': this.$store.state.search},
      })
        .then((response) => {
          console.log(response);
          this.articles = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  mounted() {
    this.makelist();
    this.getArticles();
  },

};
</script>

<style>
a {
    text-decoration: none;
    color: black;
}

</style>