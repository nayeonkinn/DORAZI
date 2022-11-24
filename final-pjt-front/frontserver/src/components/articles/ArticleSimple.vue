<template>
  <div class="movie-card" @click="todetail">
    <div class="card-head2">
      <img class="card-img align-center" :src="poster_path" alt="poster_img" />
      <div class="card-overlay">
        <div class="bookmark">
            <span>{{ updatedate }}</span>
        </div>
        <div class="rating">
          <ion-icon name="star-outline"></ion-icon>
          <span>{{ rating }}</span>
        </div>
        <div class="play" style="font-size: large">
          <p style="font-size: large">{{ content }}</p>
        </div>
      </div>
    </div>
    <div class="card-body">
      <h3 class="card-title1" @click="toprofile">{{ writer }}</h3>

      <div class="card-info">
        <span class="genre"> {{ moviename }} </span>
        <span class="year">{{ updatedate }}</span>
      </div>
    </div>
  </div>
</template>
  
  <script>
export default {
  name: "ArticleSimple",
  props: {
    article: Object,
  },
  data() {
    return {
      now: false,
      articlecontent: null,
    };
  },
  computed: {
    writer() {
      return this.article.user.username;
    },
    updatedate() {
      return this.article.updated_at.slice(0, 10);
    },
    spoiler() {
      return this.article.spoiler;
    },
    likenum() {
      return this.article.like_users.lenght;
    },
    content() {
      return this.article.content;
    },
    rating() {
      return this.article.rating;
    },
    poster_path() {
      return (
        "https://image.tmdb.org/t/p/original/" + this.article.movie.poster_path
      );
    },
    moviename() {
      return this.article.movie.title

    }
  },
  methods: {
    todetail() {
      this.$store.state.articledetail = this.article;
      this.$router.push({
        name: "ArticleDetailView",
        params: { article_id: this.article.id },
      });
    },
    toprofile() {
      this.$router.push({
        name: "ProfileView",
        params: { username: this.writer },
      });
    },
  },
};
</script>
  
<style>
.movie-card .card-overlay {
  position: absolute;
  inset: 1;
  opacity: 1;
  scale: 1;
  backdrop-filter: blur(5px) brightness(70%);
}
</style>