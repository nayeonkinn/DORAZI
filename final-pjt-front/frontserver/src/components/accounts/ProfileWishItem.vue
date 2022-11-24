<template>
  <div class="movie-card" @click="tomovie">
    <div class="card-head1">
      <img class="card-img align-center" :src="poster_path" alt="poster_img" />
    </div>
    <div class="card-body">
      <h3 class="card-title1">{{ movie_title }}</h3>

      <div class="card-info">
        <!-- <span class="genre"> {{ genres }} </span> -->
        <span class="year">{{ movie_release_date }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfileWishItem",
  props: {
    wish: Object,
  },
  computed: {
    poster_path() {
      return "https://image.tmdb.org/t/p/original/" + this.wish.poster_path;
    },
    movie_title() {
      return this.wish.title;
    },
    movie_release_date() {
      return this.wish.release_date.substr(0, 4);
    },
  },
  methods: {
    tomovie() {
      this.$router.push({
        name: "MovieDetailView",
        params: { movie_pk: this.wish.id },
      });
    },
  },
};
</script>

<style>
</style>