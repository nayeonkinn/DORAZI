<template>
  <div>
    <app-nav/>
    <router-view/>
  </div>
</template>

<script>
import AppNav from '@/components/AppNav'

export default {
  components: {
    AppNav,
  }
}
</script>

<style>
  @import '@/assets/main.css';

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
