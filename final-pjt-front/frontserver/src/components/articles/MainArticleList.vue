<template>
  <div>
    <MainArticleForm v-if="formOn" @create-article="createArticle" />
    <div v-if="!recommendDiv" class="container">
      <div class="boxForLine mb-5"></div>
    </div>
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
  props: {
    recommendDiv: Boolean,
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
      alert('후기가 삭제되었습니다.')
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

.boxForLine {
  height: 0.5px;
  outline: none;
  background: white;
  border-radius: 5px;
}

</style>