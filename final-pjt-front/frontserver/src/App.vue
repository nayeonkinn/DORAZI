<template>
  <div id="app" class="p-2" style="min-height: 100vh">
    <app-nav class='mb-3'/>
    <div class="p-5">
      <router-view />
    </div>
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
