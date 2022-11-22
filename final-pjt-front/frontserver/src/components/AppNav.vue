<template>
  <nav class="navbar navbar-expand">
    <div class="container-fluid">
      <router-link class="navbar-brand text-white" :to="{ name: 'MainView' }"
        >cinema.log
      </router-link>

      <form
        id="searchForm"
        class="d-flex m-3 d-none d-md-block"
        @submit.prevent="search"
      >
        <button id="searchBtn" class="btn btn-link" type="submit">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-search"
            viewBox="0 0 16 16"
          >
            <path
              d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"
            />
          </svg>
        </button>
        <input
          id="searchInput"
          type="text"
          class="form-control"
          placeholder="Search"
          v-model="q"
        />
      </form>

      <div class="d-flex" style="margin-top: 7px;">
        <router-link :to="{ name: 'SearchView' }" class="d-block d-md-none px-2">
          <svg
            id="searchBtnSmall"
            xmlns="http://www.w3.org/2000/svg"
            width="25"
            height="25"
            fill="currentColor"
            class="bi bi-search"
            viewBox="0 0 16 16"
          >
            <path
              d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"
            />
          </svg>
        </router-link>

        <router-link
          id="profileBtn"
          :to="{ name: 'ProfileView', params: { username: username } }"
          class="d-flex p-2"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="25"
            height="25"
            fill="currentColor"
            class="bi bi-person-circle mx-2"
            viewBox="0 0 16 16"
          >
            <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" />
            <path
              fill-rule="evenodd"
              d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"
            />
          </svg>
          {{ usernameField }}
        </router-link>
        <b-dropdown right size="lg" variant="link" no-caret>
          <template #button-content>
            <svg
              id="settingBtn"
              xmlns="http://www.w3.org/2000/svg"
              width="25"
              height="25"
              fill="currentColor"
              class="bi bi-gear-fill"
              viewBox="0 0 16 16"
            >
              <path
                d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"
              />
            </svg>
          </template>
          <b-dropdown-item
            class="dropdown-item"
            v-if="!isLogin"
            :to="{ name: 'SignupView' }"
            >Signup
          </b-dropdown-item>
          <b-dropdown-item
            class="dropdown-item"
            v-if="!isLogin"
            :to="{ name: 'LoginView' }"
            >Login</b-dropdown-item
          >
          <b-dropdown-item
            class="dropdown-item"
            v-if="isLogin"
            :to="{ name: 'SettingView' }"
            >Setting</b-dropdown-item
          >
          <b-dropdown-item class="dropdown-item" v-if="isLogin" @click="logout">
            Logout</b-dropdown-item
          >
        </b-dropdown>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "AppNav",
  data() {
    return {
      q: null,
    };
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
    username() {
      return this.$store.state.username;
    },
    usernameField() {
      return this.isLogin ? this.username : "로그인하세요";
    },
  },
  methods: {
    logout() {
      this.$store.dispatch("logout");
      this.$router.push({ name: "LoginView" }).catch(() => {});
    },
    search() {
      console.log(this.q);
      if (!this.q) {
        alert("검색어를 입력해 주세요");
      } else {
        this.$store.commit("SEARCH", this.q);
        this.$router.push({ name: "SearchResultView", params: { q: this.q } });
        this.$router.go();
      }
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Crimson+Text:wght@700&family=Gothic+A1&family=Noto+Sans+KR&display=swap");

nav {
  padding: 30px;
}

.navbar-brand {
  font-family: "Crimson Text", serif;
  font-size: 40px !important;
  padding-bottom: 10px !important;
}

#searchForm {
  position: relative;
  height: 40px;
  width: 600px;
}

#searchBtn {
  position: absolute;
  left: 2px;
  bottom: 1.5px;
  color: white;
}

#searchBtnSmall {
  color: white;
  margin-top: 8px;
}

#searchInput {
  height: 40px;
  border: none;
  border-radius: 30px;
  text-indent: 30px;
  vertical-align: middle;
  color: white;
  background-color: rgb(53, 53, 53);
}

#searchInput::placeholder {
  color: white;
}

#settingBtn {
  color: white;
  margin-bottom: 9px;
}

#profileBtn {
  color: white;
  text-decoration: none;
  font-size: 20px;
}
</style>