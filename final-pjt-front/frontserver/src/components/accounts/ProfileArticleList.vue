<template>
  <div class="my-5">
    <hr><br><br>
    <section class="movies">
      <p class="profileTitle"> {{ username }}님이 작성한 후기</p>
      <div class="movies-grid2">
        <ProfileArticleItem
          v-for="article in articles_list"
          :key="`article-${article.id}`"
          :article="article"
        />
      </div>
      <hr />
    </section>
  </div>
</template>

<script>
import ProfileArticleItem from "@/components/accounts/ProfileArticleItem";

export default {
  name: "ProfileArticleList",
  components: {
    ProfileArticleItem,
  },
  props: {
    articles_list: Array,
  },
  computed: {
    username() {
      return this.$store.state.username;
    },
  },
};
</script>

<style>
.movies-grid2 {
  padding: 10px;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  grid-template-rows: repeat(auto-fill, minmax(400px, 1fr));
  gap: 40px;
  margin-bottom: 60px;
}

.profileTitle {
  text-align: left;
  padding-left: 13px;
  font-size: 20px;

}
</style>