<template>
  <div class="container3">
    <section class="movies">
      <h1>추천 영화 리스트</h1>
      <h2> 내가 검색해 본 영화들 </h2>
      <div class="movies-grid">
        <Movie v-for="movie in recommendlist" :key="movie.id" :movie="movie" />
      </div>
      <hr>
      <h2> 친구가 리뷰를 작성한 영화들</h2>
      <div class="movies-grid">
        <Movie v-for="movie in friend_recommendlist" :key="movie.id" :movie="movie" />
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
      recommendlist: [],
      friend_recommendlist: [],
    };
  },

  methods: {
    makelist() {
      axios({
        method: 'get',
        url: `${API_URL}/profile/recommend/`,
      })
      .then((res) => {
        console.log(res.data);
        this.recommendlist = res.data
      })
      .catch((err) =>{
        console.log(err);
      })
    },
    friendlist() {
      axios({
        method: 'get',
        url: `${API_URL}/profile/recommend_friend/`,
      })
      .then((res) => {
        console.log(res.data);
        this.friend_recommendlist = res.data
      })
      .catch((err) =>{
        console.log(err);
      })
  },
  created(){
    this.makelist()
    this.friendlist()

  }
}}
</script>

<style>
  @import '@/assets/main.css';

</style>