<template>
  <div>
    <MainArticleForm v-if="formOn" @create-article="createArticle" />
    <MainArticleItem
      v-for="article in articles"
      :key="`article-${article.id}`"
      :article="article"
      @delete-article="deleteArticle"
      @update="getArticles"
    />
  </div>
</template>

<script>
import axios from "axios";
import MainArticleForm from "@/components/articles/MainArticleForm";
import MainArticleItem from "@/components/articles/MainArticleItem";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MainArticleList",
  components: {
    MainArticleForm,
    MainArticleItem,
  },
  data() {
    return {
      articles: null,
      formOn: true,
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
          if (!this.articles) {
            this.$emit('no-articles')
            this.formOn = false
          }
        });
    },
    deleteArticle(articleId) {
      let index;
      this.articles.forEach((article, idx) => {
        if (article.id === articleId) {
          index = idx;
        }
      });
      this.articles.splice(index, 1);
    },
    createArticle(article) {
      this.articles.unshift(article);
    }
  },
  created() {
    this.getArticles();
  },
};
</script>

<style>
</style>