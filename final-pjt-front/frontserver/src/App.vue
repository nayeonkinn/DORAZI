<template>
<<<<<<< HEAD
  <div>
    <app-nav/>
    <router-view/>
=======
  <div id="app" class="p-2">
    <app-nav />
    <router-view />
>>>>>>> 738fde6862379ec66a74e7f90ee4aa2edf878ef8
  </div>
</template>

<script>
import AppNav from "@/components/AppNav";

export default {
  components: {
    AppNav,
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Gothic+A1&family=Noto+Sans+KR&display=swap");

#app {
  font-family: "Gothic A1", sans-serif;
  /* font-family: 'Noto Sans KR', sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background-color: black;
}
</style>
