<template>
  <div>
    <p @click="goProfile(article.user.username)">{{ article.user.username }}</p>
    <img :src="posterPath" style="width: 150px; height: 200px" />
    <p>{{ article.movie.title }}</p>
    <p>{{ article.content.substring(0, 10) }}...</p>
    <p>좋아요 {{ article.like_count }}</p>
    <button @click="goDetail(article.id)">더보기</button>
    <hr />
  </div>
</template>

<script>
export default {
  name: "RecoArticlesItem",
  props: {
    article: Object,
  },
  computed: {
    posterPath() {
      return (
        "https://image.tmdb.org/t/p/original/" + this.article.movie.poster_path
      );
    },
  },
  methods: {
    goDetail(articleId) {
      this.$router.push({
        name: "ArticleDetailView",
        params: {
          article_id: articleId,
        },
      });
    },
    goProfile(username) {
      this.$router.push({
        name: "ProfileView",
        params: {
          username: username,
        },
      });
    },
  },
};
</script>

<style>
</style>