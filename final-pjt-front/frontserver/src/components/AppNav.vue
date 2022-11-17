<template>
  <nav>
    <router-link to="/">Home</router-link>
    <router-link v-if="!isLogin" :to="{ name: 'SignupView' }">Signup</router-link>
    <router-link v-if="!isLogin" :to="{ name: 'LoginView' }">Login</router-link>
    <button v-if="isLogin" @click="logout">Logout</button>
    <router-link v-if="isLogin" :to="{ name: 'UserUpdateView' }">Change</router-link>
    <router-link v-if="isLogin" :to="{ name: 'ProfileView', params: {'username': username }}">My Profile</router-link>
  </nav>
</template>

<script>
export default {
  name: 'AppNav',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    username() {
      return this.$store.state.username
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
    }
  }
}
</script>

<style>
nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>