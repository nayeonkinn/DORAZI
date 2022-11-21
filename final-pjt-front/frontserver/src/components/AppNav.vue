<template>
  <nav class="navbar navbar-expand-lg bg-light">
  <div class="container-fluid">
    <router-link class="navbar-brand" :to="{ name:'MainView' }" >Cinema.log</router-link>
    <!-- <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button> -->
    <div class="navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item d-flex">
          <router-link class="nav-link" v-if="!isLogin" :to="{ name: 'SignupView' }">Signup</router-link>
          <router-link class="nav-link" v-if="!isLogin" :to="{ name: 'LoginView' }" >Login</router-link>
          <router-link class="nav-link active" :to="{ name:'MovieView' }"> Movie </router-link>  
        </li>
        <div>
        <b-dropdown class="nav-item dropdown m-2" id="dropdown-offset" offset="25" text="User" >
          <b-dropdown-item class="dropdown-item" v-if="!isLogin" :to="{ name: 'SignupView' }" >Signup </b-dropdown-item>
          <b-dropdown-item class="dropdown-item" v-if="!isLogin" :to="{ name: 'LoginView' }" >Login</b-dropdown-item>
          <b-dropdown-item class="dropdown-item" v-if="isLogin" :to="{ name: 'SettingView' }">Setting</b-dropdown-item>
          <b-dropdown-item class="dropdown-item" v-if="isLogin" :to="{ name: 'ProfileView', params: {'username': username }}">Profile</b-dropdown-item>
          <b-dropdown-item class="dropdown-item" v-if="isLogin" @click="logout"> Logout</b-dropdown-item>
        </b-dropdown>
      </div>

      </ul>
        <router-link class="nav-link active" :to="{ name: 'SearchView', params: { q: search}}"> 
        </router-link>
        <form class="container d-flex" @submit.prevent="search">
            <input class="form-control me-2" placeholder="Search" v-model="q">
            <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
    </div>
  </div>
</nav>
</template>

<script>
export default {
  name: 'AppNav',
  data() {
    return {
      q: null,
    }
  },

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
      this.$router.push({ name: 'MainView' })
    },
    search() {
      console.log(this.q)
      this.$store.commit('SEARCH', this.q)
      this.$router.push({ name: 'SearchView' , params: { "q": this.q}})
      this.$router.go()
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