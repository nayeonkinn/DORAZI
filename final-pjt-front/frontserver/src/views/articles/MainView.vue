<template>
  <div>
    <MainArticleList v-if="isLoggedIn"/>
  </div>
</template>

<script>
import MainArticleList from '@/components/articles/MainArticleList';

export default {
  name: "MainView",
  components: {
      MainArticleList
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLogin
    }
  },
}
</script>
