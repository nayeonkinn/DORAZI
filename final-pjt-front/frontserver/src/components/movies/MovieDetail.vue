<template>
  <div>
    <div
      class="single"
      :style="{
        'background-image': `url(https://image.tmdb.org/t/p/original/${this.backdrop})`,
      }"
    ></div>
    <img :src="poster" class="poster" alt="poster" />
    <div>{{ movietitle }}</div>
    <div>{{ release_date }}</div>
    <div>{{ overview }}</div>

    <!-- <div>
      <b-button id="show-btn" @click="showModal">Open Modal</b-button>

      <b-modal ref="my-modal" hide-footer title="Using Component Methods">
        <div class="d-block text-center">
          <h3>게시글 작성</h3>
          <form @submit.prevent="createArticle">
            <label for="title">제목 : </label>
            <input type="text" id="title" v-model.trim="articletitle" /><br />
            <label for="content">내용 : </label>
            <textarea
              id="content"
              cols="30"
              rows="10"
              v-model="articlecontent"
            ></textarea
            ><br />
            <b-button
            class="mt-3"
            variant="outline-success"
            block
            @click="createArticle"
            >
            작성
          </b-button>
          <b-button
          class="mt-3"
          variant="outline-danger"
          block
          @click="hideModal"
          >
          취소
        </b-button>
      </form>
    </div>
      </b-modal>
    </div> -->
    <div>
      <h3>게시글 작성</h3>
      <form @submit.prevent="createArticle">
        <label for="content">내용 : </label>
        <textarea
          id="content"
          cols="30"
          rows="10"
          v-model="articlecontent"
        ></textarea
        ><br />
        <input type="submit" id="submit" />
      </form>
    </div>
    <div class="cotainer">
      <ArticleList
        v-for="article in articlelist.slice().reverse()"
        :key="article.id"
        :article="article"
        @update="detaildata"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
import ArticleList from "@/components/articles/ArticleList";

export default {
  name: "MovieDetail",
  components: {
    ArticleList,
  },
  data() {
    return {
      movieinfo: null,
      poster: null,
      backdrop: null,
      movietitle: null,
      overview: null,
      release_date: null,
      articletitle: null,
      articlecontent: null,
      articlelist: [],
    };
  },
  methods: {
    showModal() {
      this.$refs["my-modal"].show();
    },
    hideModal() {
      this.$refs["my-modal"].hide();
    },
    createArticle() {
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
          rating: 5
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          this.articlecontent = null;
          this.detaildata();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    detaildata() {
      const movie_pk = this.$route.params.movie_pk;
      axios({
        method: "get",
        url: `${API_URL}/movies/${movie_pk}/`,
        data: {},
      })
        .then((res) => {
          console.log(res);
          this.movieinfo = res.data;
          this.poster = `https://image.tmdb.org/t/p/w185/${res.data.poster_path}`;
          this.backdrop = this.movieinfo.backdrop_path;
          this.movietitle = this.movieinfo.title;
          this.overview = this.movieinfo.overview;
          this.release_date = this.movieinfo.release_date.slice(0, 4);
          this.articlelist = this.movieinfo.articles_list;
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
.poster {
  width: 15%;
  height: 15%;
}
</style>