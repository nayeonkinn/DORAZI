<template>
  <div>
    <section class="movies">
      <h1>작성한 후기</h1>
      <div class="movies-grid">
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
</style>