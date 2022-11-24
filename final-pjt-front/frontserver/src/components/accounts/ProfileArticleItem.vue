<template>
  <div class="movie-card" @click="toarticle">
    <div class="card-head2">
      <img class="card-img align-center" :src="poster_path" alt="poster_img" />
      <div class="card-overlay">
        <div class="bookmark">
          <ion-icon name="bookmark-outline"></ion-icon>
        </div>

        <div class="rating">
          <ion-icon name="star-outline"></ion-icon>
          <span>{{ rating }}</span>
        </div>

        <div class="play" style="font-size:large">
          <p>{{ content }}</p>
        </div>
      </div>
    </div>
    <div class="card-body">
      <h3 class="card-title1">{{ movie_title }}</h3>

      <div class="card-info">
        <!-- <span class="genre"> {{ genres }} </span> -->
        <span class="year">{{ movie_release_date }}</span>
      </div>
    </div>
  </div>
  <!-- <img :src="poster_path" alt="poster_img" style="width: 300px; height: 400px;"> -->
</template>

<script>
export default {
  name: "ProfileArticleItem",
  props: {
    article: Object,
  },
  computed: {
    poster_path() {
      return (
        "https://image.tmdb.org/t/p/original/" + this.article.movie.poster_path
      );
    },
    movie_title() {
      return this.article.movie.title;
    },
    movie_release_date() {
      return this.article.movie.release_date.substr(0, 4);
    },
    content() {
      return this.article.content;
    },
		rating() {
			return this.article.rating
		}
  },
  methods: {
    toarticle() {
      // console.log(this.article)
      this.$store.state.articledetail = this.article;
      this.$router.push({
        name: "ArticleDetailView",
        params: { article_id: this.article.id },
      });
    },
  },
  created() {
    // console.log(this.article)
  },
};
</script>

<style>
.movie-card .card-head2 {
  position: relative;
  height: 350px;
  border-radius: 15px;
  margin-bottom: 15px;
  overflow: hidden;
}
.play {
  width: 250px; /* 너비는 변경될수 있습니다. */
  height: 200px;
  line-height: 20px;
  overflow: hidden; /* 내용이 길면 감춤니다 */
  display: -webkit-box;
  -webkit-line-clamp: 10;
  -webkit-box-orient: vertical;
}
</style>