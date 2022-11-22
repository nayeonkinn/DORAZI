<template>
  <div>
    <div>

      <div
      class="single"
      :style="{
        'background-image': `url(https://image.tmdb.org/t/p/original/${this.backdrop})`,
      }"
    ></div>
    <div class="movie-infos">
      <header>
        <img :src="poster" class="poster movie-poster" alt="poster" />
        <div class="movie-release">
          <div class="title">{{ release_date }}</div>
          <span></span>
        </div>
      </header>
      <div class="movie-info-all">
      </div>
      <div class="basic-info row">
        <div class="title col-10">{{ movietitle }}
        </div>
        <button @click="wishToggle" class="flex-right col-2"> Wish </button>
        <div class="info-summary">
          <div class="story-summary">
            {{ overview }}
          </div>
        </div>

      </div>
    </div>
  </div>
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
    wishToggle () { 
      axios({
        method: "POST",
        url: `${API_URL}/articles/create/${this.movieinfo.id}/`,
        data: {
          content: this.articlecontent,
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
  mounted() {
    this.detaildata()
  },

}
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

<style lang="scss" scoped>
.movie-infos {
  display: flex;
  justify-content: center;
  width: 100vw;
  height: 220px;
  margin: 0 auto 20px;
  padding: 0 200px;
  background-color: white;
  border-bottom: 1px solid #e3e3e3;

  > header {
    position: relative;

    .movie-poster {
      width: 165px;
      height: 234px;
      margin-top: -36px;
      border: 2px solid white;
      border-radius: 5px;
    }

    .movie-release {
      position: absolute;
      width: 200px;
      top: -25px;
      left: 190px;
      text-align: left;
      color: white;
      font-size: small;
      font-weight: 400;

      > span {
        opacity: 0.75;
        &:first-child {
          opacity: 0.4;
        }
      }
    }
  }

  .movie-info-all {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin: 16px 0 23px 25px;
    text-align: left;

    .movie-title {
      .title {
        font-size: 34px;
        font-weight: 700;
      }

      .text {
        width: 780px;
        margin: 6px 0;
        font-size: 17px;
        color: #7f7f7f;
      }
    }

    .rating-star {
      width: 769px;
      font-size: 19px;

      &::before {
        content: '';
        display: block;
        width: 100%;
        margin-bottom: 10px;
        border-top: 1px solid #f0f0f0;
      }
      &::after {
        content: '';
        display: block;
        width: 100%;
        margin-top: 8px;
        border-bottom: 1px solid #f0f0f0;
      }

      .rating-mystar {
        color: pink;
        margin-left: 16px;
      }
    }
  }
}

.basic-info {
  margin: 20px;

  .title {
    margin: 20px 0 20px;
  }

  .info-summary {
    position: relative;
    width: 598px;
    margin: 10px 0 30px;

    &::after {
      content: '';
      display: block;
      margin: 0 auto;
      width: 598px;
      border-bottom: 1px solid #f0f0f0;
    }

    .little-summary {
      width: 598px;
      margin-top: 8px;
    }

    .story-summary {
      position: relative;
      display: -webkit-box;
      margin: 15px 0;
      max-height: 4.5rem;
      line-height: 23px;
      overflow: hidden;
      -webkit-line-clamp: 3; /* 라인수 */

      &.show {
        display: block;
        max-height: none;
        overflow: auto;
        -webkit-line-clamp: unset;
      }
    }

    > button {
      position: absolute;
      bottom: 19px;
      right: 0;
      max-height: 2rem;
      line-height: 23px;
      padding-left: 20px;
      background: rgb(2, 0, 36);
      background: linear-gradient(
        90deg,
        rgba(2, 0, 36, 1) 0%,
        rgba(255, 255, 255, 0) 0%,
        rgba(255, 255, 255, 1) 18%
      );
      font-size: 15px;
      font-weight: 500;
      color: pink;
      cursor: pointer;

      &.hide {
        display: none;
      }
    }
  }
}
</style>