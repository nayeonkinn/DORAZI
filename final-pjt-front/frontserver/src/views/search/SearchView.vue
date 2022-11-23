<template>
  <div class="container">
    <search class="m-3 mb-5 d-block d-md-none d-flex flex-column align-items-center">
      <form id="searchForm" @submit.prevent="search">
        <button id="searchBtn" class="btn btn-link" type="submit">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-search"
            viewBox="0 0 16 16"
          >
            <path
              d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"
            />
          </svg>
        </button>
        <input
          id="searchInput"
          type="text"
          class="form-control"
          placeholder="영화, 후기, 유저를 검색해보세요"
          v-model="q"
        />
      </form>
    </search>
    <SearchResultView v-if="resultOn"></SearchResultView>
  </div>
</template>

<script>
import SearchResultView from "@/views/search/SearchResultView";

export default {
  name: "SearchView",
  components: {
    SearchResultView,
  },
  data() {
    return {
      q: null,
    };
  },
  computed: {
    resultOn() {
      return this.$store.state.resultOn;
    },
  },
  methods: {
    search() {
      console.log(this.q);
      if (!this.q.trim()) {
        alert("검색어를 입력해 주세요.");
        this.q = null;
      } else {
        this.$store.commit("SEARCH", this.q);
        this.$router.go();
      }
    },
  },
};
</script>

<style>
</style>