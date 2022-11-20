<template>
  
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "ArticleDetail",

  data() {
    return {
      articleinfo: null,
      poster: null,
      movietitle: null,
      user: null,
      updatedate : null,
      
    };
  },
  methods: {
    showModal() {
      this.$refs["my-modal"].show();
    },
    hideModal() {
      this.$refs["my-modal"].hide();
    },
    createComment() {
      const content = this.articlecontent;
      if (!content) {
        alert("내용을 입력해주세요");
        return;
      }
      axios({
        method: "POST",
        url: `${API_URL}/articles/create/${this.movieinfo.id}/`,
        data: {
          content: content,
          spoiler: false,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          this.articlecontent = null;
          this.detaildata()

        })
        .catch((err) => {
          console.log(err);
        });
    },
    detaildata() {
      const article_pk = this.$route.params.article_pk;
    axios({
      method: "get",
      url: `${API_URL}/articles/${article_pk}/`,
      data: {},
    })
      .then((res) => {
        console.log(res);
        this.articleinfo = res.data;
        this.poster = `https://image.tmdb.org/t/p/w185/${res.data.poster_path}`;
        this.backdrop = this.movieinfo.backdrop_path;
        this.movietitle = this.movieinfo.title;
        this.overview = this.movieinfo.overview;
        this.release_date = this.movieinfo.release_date.slice(0, 4);
        this.articlelist = this.movieinfo.articles_list
      })
      .catch((err) => {
        console.log(err);
      });
    }
  },
  created() {
    this.detaildata()
  },
};
</script>


<style>

</style>