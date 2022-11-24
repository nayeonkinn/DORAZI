<template>
  <div class="container" style="min-height: 100vh">
    <img
      v-if="fakeLogo"
      @click="changeLogo"
      class="img mb-5"
      src="@/assets/fake_logo.png"
      alt="fake logo"
      style="width: 250px; margin-top: 100px"
      />
      <img
      v-else
      @click="changeLogo"
      class="img mb-5"
      src="@/assets/real_logo.png"
      alt="real logo (happy developers)"
      style="width: 250px; margin-top: 100px"
    />
    <h1 class="mb-5">로그인하고 친구들과 영화로 대화를 나눠 보세요</h1>
    <div class="d-flex justify-content-center align-items-center">
      <div id="loginForm" style="width: 500px">
        <form @submit.prevent="login">
          <div class="form-floating mb-3">
            <input
              v-model.trim="username"
              type="text"
              class="form-control"
              id="floatingInput"
              placeholder="아이디"
            />
            <label for="floatingInput">아이디</label>
          </div>
          <div class="form-floating mb-4">
            <input
              v-model.trim="password"
              type="password"
              class="form-control"
              id="floatingPassword"
              placeholder="비밀번호"
            />
            <label for="floatingPassword">비밀번호</label>
          </div>
          <div class="d-grid gap-2 mb-4">
            <button id="loginBtn" class="btn">로그인</button>
          </div>
        </form>
        <p style="font-size: 18px" class="mt-5">
          계정이 없으신가요?
          <router-link id="toSignup" :to="{ name: 'SignupView' }"
            >회원가입</router-link
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      username: null,
      password: null,
      fakeLogo: true,
    };
  },
  methods: {
    login() {
      if (!this.username) {
        alert("아이디를 입력해 주세요.");
        return;
      } else if (!this.password) {
        alert("비밀번호를 입력해 주세요.");
        return;
      }

      const payload = {
        username: this.username,
        password: this.password,
      };
      this.$store.dispatch("login", payload);
      this.username = null;
      this.password = null;

      this.$router.push({ name: "MainView" }).catch(() => {});
      // console.log(this.$store.getters.isLogin)
    },
    changeLogo() {
      this.fakeLogo =!this.fakeLogo;
    }
  },
};
</script>

<style>
label {
  color: black;
}

#loginBtn {
  height: 58px;
  color: white;
  background-color: rgb(53, 53, 53);
  z-index: 1;
}

.img {
  animation: rotate_image 6s linear infinite;
  transform-origin: 50% 50%;
}

@keyframes rotate_image {
  100% {
    transform: rotate(360deg);
  }
}

#toSignup {
  color: rgb(158, 158, 158);
  text-decoration: none;
}
</style>