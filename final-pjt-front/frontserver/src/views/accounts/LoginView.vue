<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username">

      <label for="password">password : </label>
      <input type="password" id="password" v-model="password">

      <input type="submit" value="Login">
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('login', payload)
      this.$router.push({ name: 'MainView'}).catch(() => {})
      // console.log(this.$store.getters.isLogin)
    }
  }
}
</script>

<style>

</style>