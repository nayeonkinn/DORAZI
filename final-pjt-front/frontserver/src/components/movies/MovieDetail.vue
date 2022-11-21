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

    <div>
      <b-button id="show-btn" @click="showModal">Open Modal</b-button>

      <b-modal ref="my-modal" hide-footer title="Using Component Methods">
        <div class="d-block text-center">
          <h3>게시글 작성</h3>
          <form @submit.prevent="createArticle">
            <label for="content">내용 : </label>
            <textarea
              id="content"
              cols="30"
              rows="10"
              v-model="articlecontent"
            ></textarea>
            <!-- 별점 -->
            <!-- https://melthleeth.tistory.com/entry/HTML-CSS%EB%A1%9C-%EB%B3%84%EC%B0%8D%EA%B8%B0-Star-Rating -->
            <div class="star-rating space-x-4 mx-auto">
              <input type="radio" id="5-stars" name="rating" value="5" v-model="ratings"/>
              <label for="5-stars" class="star pr-4">★</label>
              <input type="radio" id="4-stars" name="rating" value="4" v-model="ratings"/>
              <label for="4-stars" class="star">★</label>
              <input type="radio" id="3-stars" name="rating" value="3" v-model="ratings"/>
              <label for="3-stars" class="star">★</label>
              <input type="radio" id="2-stars" name="rating" value="2" v-model="ratings"/>
              <label for="2-stars" class="star">★</label>
              <input type="radio" id="1-star" name="rating" value="1" v-model="ratings" />
              <label for="1-star" class="star">★</label>
            </div>
            <!-- 스포일러 여부 -->
            <label for="spoiler"> 스포일러 여부 </label>
            <input type="checkbox" v-model="spoiler" true-value="yes" false-value="no" name="spolier">

            <br/>
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
    </div>
    <!-- <div>
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
    </div> -->
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
      ratings : 0,
      spoiler : false,
    };
  },
  methods: {
    getActiveStar(index) {
      this.score = index + 1;
    },
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
          spoiler: this.spoiler,
          rating: this.ratings,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          this.articlecontent = null;
          this.detaildata();
          this.hideModal()
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

<style >
.poster {
  width: 15%;
  height: 15%;
}
.star-rating {
  display: flex;
  flex-direction: row-reverse;
  font-size: 2.25rem;
  line-height: 2.5rem;
  justify-content: space-around;
  padding: 0 0.2em;
  text-align: center;
  width: 5em;
}
 
.star-rating input {
  display: none;
}
 
.star-rating label {
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 2.3px;
  -webkit-text-stroke-color: #2b2a29;
  cursor: pointer;
}
 
.star-rating :checked ~ label {
  -webkit-text-fill-color: gold;
}
 
.star-rating label:hover,
.star-rating label:hover ~ label {
  -webkit-text-fill-color: #fff58c;
}

</style>