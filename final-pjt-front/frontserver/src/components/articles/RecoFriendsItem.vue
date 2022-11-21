<template>
  <div>
    <p @click="goProfile(friend.username)">{{ friend.username }}</p>
    <p>팔로워 : {{ friend.followers.length }}</p>
    <div v-if="friend.hot_article[0]">
      <p>대표 게시글</p>
      <img :src="posterPath" style="width: 150px; height: 200px" />
      <p>{{ friend.hot_article[0].movie.title }}</p>
      <p>
        {{ friend.hot_article[0].content.substring(0, 10) }}...
        <button @click="goDetail(friend.hot_article[0].id)">더보기</button>
      </p>
    </div>
    <hr />
  </div>
</template>

<script>
export default {
  name: "RecoFriendsItem",
  props: {
    friend: Object,
  },
  computed: {
    posterPath() {
      return (
        "https://image.tmdb.org/t/p/original/" + this.friend.hot_article[0].movie.poster_path
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