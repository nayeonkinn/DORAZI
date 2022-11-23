<template>
  <div class="container" style="min-height: 100vh">
    <img
      v-if="fakeLogo"
      @click="changeLogo"
      class="img mb-5"
      src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ff60be88-063a-4ff0-a57f-ccab09f7997c/logo1_wh.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221123T122435Z&X-Amz-Expires=86400&X-Amz-Signature=d25ccbefa73ad508a2ac003fe9edb607c3396ab14f49ea860de31aedecc1ddd0&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22logo1_wh.png%22&x-id=GetObject"
      alt="fake logo"
      style="width: 250px; margin-top: 270px"
      />
      <img
      v-else
      @click="changeLogo"
      class="img mb-5"
      src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8fdba63a-7c45-4094-bb51-8a4f5723a6ae/Picture1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221123T123549Z&X-Amz-Expires=86400&X-Amz-Signature=31fd3855f09fc521fd15210886d7265ecb64c2ea48589c1dde6035316c0c4f8f&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Picture1.png%22&x-id=GetObject"
      alt="real logo (happy developers)"
      style="width: 250px; margin-top: 270px"
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