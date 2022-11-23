<template>
  <div class="movie-card" @click="toarticle">
    <div class="card-head1">
      <img class="card-img align-center" :src="poster_path" alt="poster_img" />
      <div class="card-overlay">
        <div class="bookmark">
          <ion-icon name="bookmark-outline"></ion-icon>
        </div>

        <div class="rating">
          <ion-icon name="star-outline"></ion-icon>
          <span>{{ rating }}</span>
        </div>

        <div class="play">
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
.movie-card {
  /**
   * variable for scaling overlay element on card hover 
   */
  --scale: 0.9;

  cursor: pointer;
}
.play {
  width: 150px; /* 너비는 변경될수 있습니다. */
  height: 100px;
  line-height: 20px;
  overflow: hidden; /* 내용이 길면 감춤니다 */
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
}
</style>