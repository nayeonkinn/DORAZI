<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <label for="username">username : </label>
      <input type="text" id="username" v-model.trim="username">

      <label for="password">password : </label>
      <input type="password" id="password" v-model.trim="password">

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

      if (!username) {
        alert('아이디를 입력해 주세요.')
        return
      } else if (!password) {
        alert('비밀번호를 입력해 주세요.')
        return
      }

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