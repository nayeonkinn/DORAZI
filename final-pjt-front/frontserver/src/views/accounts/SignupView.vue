<template>
  <div>
    <h1>Signup</h1>
    <form @submit.prevent="signup">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username">

      <label for="password1">password : </label>
      <input type="password" id="password1" v-model="password1">

      <label for="password2">password confirmation : </label>
      <input type="password" id="password2" v-model="password2">

      <input type="submit" value="Signup">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signup() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      }
      this.$store.dispatch('signup', payload)
      this.$router.push({ name: 'MainView' })
    }
  }
}
</script>

<style>

</style>