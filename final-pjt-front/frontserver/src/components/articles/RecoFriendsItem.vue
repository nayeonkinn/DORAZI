<template>
  <div>
    <span @click="goProfile(friend.username)" id="userResult" class="logoFont cursorPointer">{{ friend.username }}</span>
    <p>팔로워 : {{ friend.followers.length }}</p>
    <div v-if="friend.hot_article[0]">
      <p>인기 있는 포스트 : {{ friend.hot_article[0].content.substring(0, 30) }}...
        <button class="buttons" @click="goDetail(friend.hot_article[0].id)">더보기</button>
      </p>
    </div>
    <p><br><br>-</p>
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