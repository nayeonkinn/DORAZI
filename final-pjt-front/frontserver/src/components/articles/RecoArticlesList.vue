<template>
  <div>
    <h3>RECOMMEND POPULAR ARTICLES</h3>
    <RecoArticlesItem
      v-for="article in articles"
      :key="`article-${article.id}`"
      :article="article"
    ></RecoArticlesItem>
  </div>
</template>

<script>
import axios from "axios";
import RecoArticlesItem from "@/components/articles/RecoArticlesItem";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: 'RecoArticlesList',
  components: {
    RecoArticlesItem,
  },
  data() {
    return {
      articles: null,
    };
  },
  computed: {
    token() {
      return this.$store.state.token;
    },
  },
  methods: {
    getArticles() {
      axios({
        method: "get",
        url: `${API_URL}/articles/recommend/articles/`,
        headers: {
          Authorization: `Token ${this.token}`,
        },
      })
        .then((response) => {
          // console.log(response);
          this.articles = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getArticles();
  },
}
</script>

<style>

</style>