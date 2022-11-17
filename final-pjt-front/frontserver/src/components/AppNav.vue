<template>
  <nav>
    <router-link to="/">Home</router-link>
    <router-link v-if="!isLogin" :to="{ name: 'SignupView' }">Signup</router-link>
    <router-link v-if="!isLogin" :to="{ name: 'LoginView' }">Login</router-link>
    <button v-if="isLogin" @click="logout">Logout</button>
  </nav>
</template>

<script>
export default {
  name: 'AppNav',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
      this.$router.push('home')
    }
  }
}
</script>

<style>

</style>