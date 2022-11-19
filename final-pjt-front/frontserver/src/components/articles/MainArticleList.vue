<template>
  <div>
    <MainArticleItem
			v-for="article in articles"
			:key="`article-${article.id}`"
			:article="article"
		/>
  </div>
</template>

<script>
import axios from "axios";
import MainArticleItem from "@/components/articles/MainArticleItem"

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MainArticleList",
	components: {
		MainArticleItem,
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
        url: `${API_URL}/articles/`,
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
};
</script>

<style>
</style>