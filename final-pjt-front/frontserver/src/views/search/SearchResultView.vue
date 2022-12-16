<template>
  <div class="container">
    <h1 style="margin-top: 50px">검색 결과</h1>
    <br /><br />
    <section class="movies">
      <h3 style="text-align: start; margin-left: 10px; margin-bottom: 30px">
        영화
      </h3>
      <div v-if="movies.length" class="movies-grid">
        <Movie v-for="movie in movies" :key="movie.id" :movie="movie" />
      </div>
      <div class="m-5" v-if="movieresult">검색 결과가 없습니다</div>
      <br />
      <hr />
      <br />
      <h3 style="text-align: start; margin: 60px 0px 30px 10px">게시글</h3>
      <div v-if="articles.length" class="movies-grid2">
        <ArticleSimple
          v-for="article in articles"
          :key="article.id"
          :article="article"
        />
      </div>
      <div class="m-5" v-if="articleresult">검색 결과가 없습니다</div>
      <br />
      <hr />
      <br />
      <h3 style="text-align: start; margin: 60px 0px 30px 10px">유저</h3>
      <div class="mb-5">
        <div v-if="users.length" class="movies-grid">
          <UserSearch
            class="usersResultBox"
            v-for="user in users"
            :key="user.id"
            :user="user"
          />
        </div>
        <div class="m-5" v-if="userresult">검색 결과가 없습니다</div>
      </div>
    </section>
  </div>
</template>

<script>
import Movie from "@/components/movies/Movie";
import ArticleSimple from "@/components/articles/ArticleSimple";
import UserSearch from "@/components/accounts/UserSearch";

import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "SearchResultView",
  components: {
    Movie,
    ArticleSimple,
    UserSearch,
  },
  data() {
    return {
      movies: [],
      articles: [],
      users: [],
      movieresult: false,
      articleresult: false,
      userresult: false,
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
        params: { search: this.$store.state.search },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          // console.log(res.data);
          this.movies = res.data;
          if (this.movies == false) {
            this.movieresult = true;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getArticles() {
      axios({
        method: "get",
        url: `${API_URL}/articles/search/`,
        params: { search: this.$store.state.search },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((response) => {
          // console.log(response.data);
          this.articles = response.data;
          if (this.articles == false) {
            this.articleresult = true;
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getUsers() {
      axios({
        method: "get",
        url: `${API_URL}/profile/search/`,
        params: { search: this.$store.state.search },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((response) => {
          // console.log(response.data);
          this.users = response.data;
          if (this.users == false) {
            this.userresult = true;
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  mounted() {
    this.makelist();
    this.getArticles();
    this.getUsers();
  },
};
</script>

<style>

a {
  text-decoration: none;
  color: black;
}

.usersResultBox {
  width: 100%;
  height: 100px;
}
</style>