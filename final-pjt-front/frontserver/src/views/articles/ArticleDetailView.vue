<template>
  <div>
    <ArticleDetail/>
  </div>
</template>

<script>
import axios from "axios";

import ArticleDetail from "@/components/articles/ArticleDetail.vue";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "ArticleDetailView",
  components: {
    ArticleDetail,
  },
  data() {
    return {
      article: null,
    };
  },
  methods: {
    detaildata() {
      const article_pk = this.$route.params.article_id;
      axios({
        method: "get",
        url: `${API_URL}/articles/${article_pk}/`,
        // headers: {
        //   Authorization: `Token ${this.token}`,
        // },
      })
        .then((res) => {
          console.log(res);
          this.$store.state.detailarticle = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.detaildata();
  },
};
</script>

<style>
</style>