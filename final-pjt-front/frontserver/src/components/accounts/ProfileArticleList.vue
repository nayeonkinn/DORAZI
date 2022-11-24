<template>
  <div>
    <section class="movies">
      <h1>작성한 후기</h1>
      <div class="movies-grid2">
        <ProfileArticleItem
          v-for="article in articles_list"
          :key="`article-${article.id}`"
          :article="article"
        />
      </div>
      <hr>
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
  methods: {},
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
</style>