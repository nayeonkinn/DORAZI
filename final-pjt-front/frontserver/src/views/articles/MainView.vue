<template>
  <div>
    <MainArticleList v-if="isLoggedIn" @no-articles="noArticles" />
    <div v-if="recommendDiv">
      <br><RecoFriendsList/>
      <br><RecoArticlesList/>
    </div>
  </div>
</template>

<script>
import MainArticleList from "@/components/articles/MainArticleList";
import RecoFriendsList from "@/components/articles/RecoFriendsList";
import RecoArticlesList from "@/components/articles/RecoArticlesList";

export default {
  name: "MainView",
  components: {
    MainArticleList,
    RecoFriendsList,
    RecoArticlesList,
  },
  data() {
    return {
      recommendDiv: false,
    }
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLogin;
    },
  },
  methods: {
    noArticles() {
      this.recommendDiv = true;
    },
  }
};
</script>
