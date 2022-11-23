<template>
  <div class="container3">
    <!-- 영화 배너 -->
    <section class="banner">
      <div class="banner-card">
        <img class="banner-img" :src="url" alt="none">
        <div class="card-content">
          <div class="card-info">
            <div class="genre">
              <ion-icon name="film"></ion-icon>
              <span>Action/Thriller</span>
            </div>
            
            <div class="year">
              <ion-icon name="calendar"></ion-icon>
              <span>{{ titlemovie.release_date.slice(0, 4) }}</span>
            </div>
          </div>
          <h2 class="card-title"> {{ titlemovie.title }}</h2>
        </div>
      </div>
    </section>
    <!-- 영화 리스트 -->
    <section class="movies">
      <h1>추천 영화 리스트</h1>
      <h2> 내가 검색해 본 영화들 </h2>
      <div class="movies-grid">
        <Movie v-for="movie in recommendlist" :key="movie.id" :movie="movie" />
      </div>
      <hr>
      <h2> 친구가 리뷰를 작성한 영화들</h2>
      <div class="movies-grid">
        <Movie v-for="movie in friendrecommendlist" :key="movie.id" :movie="movie" />
      </div>
    </section>
  </div>
</template>

<script>
import Movie from "@/components/movies/Movie.vue";
import axios from "axios";
import _ from 'lodash'


const APIURL = 'http://127.0.0.1:8000'
export default {
  name:"MovieView",
  components:{
    Movie,

  },
  data() {
    return {
      recommendlist: [],
      friendrecommendlist: [],
      username: this.$store.state.username,
      titlemovie: [],
      url : null,
    };
  },
  computed: {
    randommovie () {
    // const friend = _.sample(this.friendrecommendlist)
    const search = _.sample(this.recommendlist)
    return search
    }
  },

  methods: {
    makelist() {
      axios({
        method: 'GET',
        url: `${APIURL}/profile/${this.username}/recommend/`,
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
        url: `${APIURL}/profile/${this.username}/recommend_friend/`,
      })
      .then((res) => {
        console.log(res);
        this.friendrecommendlist = res.data;
      })
      .catch((err) =>{
        console.log(err);
      })
  },
  changtitle(){
    axios({
        method: 'GET',
        url: `${APIURL}/movies/${this.randommovie.id}`,
      })
      .then((res) => {
        console.log(res.data);  
        this.titlemovie = res.data
        const back = this.titlemovie.backdrop_path
        this.url = `https://image.tmdb.org/t/p/original/${back}`

      })
      .catch((err) =>{
        console.log(err);
      })
  }
},
watch: {
  randommovie() {
    this.changtitle()
  }
},
  created(){
      this.makelist()
      this.friendlist()
  }
}
</script>

<style>
  @import '@/assets/main.css';

</style>