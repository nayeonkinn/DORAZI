<template>
  <div class="container p-5">
    <MainArticleList v-if="isLoggedIn" @no-articles="noArticles" :recommendDiv="recommendDiv" />
    <div v-if="recommendDiv">
      <br /><RecoFriendsList /> <br /><RecoArticlesList />
    </div>
    <button id="recoBtn" @click="goReco">오늘은 어떤 영화?</button>
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
    };
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
    goReco() {
      this.$router.push({ name: 'ReccomendView' })
    }
  },
};
</script>

<style>
#recoBtn {
  position: fixed;
  bottom: 50px;
  right: 50px;
  width: 230px;
  height: 70px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: 700;
  color: #000;
  /* background-color: #fff; */
  background-color: rgb(241, 241, 241);
  /* background-color: rgb(158, 158, 158); */
  border: none;
  border-radius: 40px;
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease 0s;
  cursor: pointer;
  outline: none;
  z-index: 1;
}

#recoBtn:hover {
  background-color: rgb(53, 53, 53);
  box-shadow: 0px 15px 20px rgba(158, 158, 158, 0.15);
  color: #fff;
  transform: translateY(-7px);
}
</style>