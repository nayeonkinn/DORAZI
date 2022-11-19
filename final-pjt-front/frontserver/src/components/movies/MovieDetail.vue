<template>
  <div>
    <div
      class="single"
      :style="{
        'background-image': `url(https://image.tmdb.org/t/p/original/${this.backdrop})`,
      }"
    ></div>
    <img :src="poster" class="poster" alt="poster" />
    <div>{{ title }}</div>
    <div>{{ movieinfo.release_date.slice(0, 4) }}</div>
    <div>{{ overview }}</div>

    <div>
      <!-- <b-button id="show-btn" @click="showModal">Open Modal</b-button>
      <b-button id="toggle-btn" @click="toggleModal">Toggle Modal</b-button>

      <b-modal ref="my-modal" hide-footer title="Using Component Methods">
        <div class="d-block text-center">
          <h3>Hello From My Modal!</h3>
        </div>
        <b-button class="mt-3" variant="outline-danger" block @click="hideModal"
          >Close Me</b-button
        >
        <b-button
          class="mt-2"
          variant="outline-warning"
          block
          @click="toggleModal"
          >Toggle Me</b-button
        >
      </b-modal> -->
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MovieDetail",
  data() {
    return {
      movieinfo: null,
      poster: null,
      backdrop: null,
      title: null,
      overview: null,
    };
  },
  // methods: {
  //   showModal() {
  //     this.$refs["my-modal"].show();
  //   },
  //   hideModal() {
  //     this.$refs["my-modal"].hide();
  //   },
  //   toggleModal() {
  //     // We pass the ID of the button that we want to return focus to
  //     // when the modal has hidden
  //     this.$refs["my-modal"].toggle("#toggle-btn");
  //   },
  // },
  created() {
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
        this.title = this.movieinfo.title;
        this.overview = this.movieinfo.overview;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style>
.poster {
  width: 15%;
  height: 15%;
}
</style>