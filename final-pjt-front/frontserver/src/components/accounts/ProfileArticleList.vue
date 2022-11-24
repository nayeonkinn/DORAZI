<template>
  <div class="my-5">
    <hr><br><br>
    <section class="movies">
      <p class="profileTitle"> {{ yourName }}님이 작성한 후기</p>
      <div v-if="articles_list.length" class="movies-grid2">
        <ProfileArticleItem
          v-for="article in articles_list"
          :key="`article-${article.id}`"
          :article="article"
        />
      </div>
      <div v-else style="margin: 100px 0px;">
        <p>앗.. 아직 없어요!</p>
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
    yourName: String,
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