<template>
  <div class="container" style="min-height: 100vh">
    <h1 class="mb-5" style="margin-top: 270px;">
      로그인하고 친구들과 영화로 대화를 나눠 보세요
    </h1>
    <div class="d-flex justify-content-center align-items-center">
      <img
        class="img"
        src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c910822a-823a-4980-8cc0-0bf381faeb47/8CB9973E-7241-4F21-9F54-9F1C32855215.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221123T001331Z&X-Amz-Expires=86400&X-Amz-Signature=6857b763fd0f8f1323e4fed976f68924ea141bf54d389e8070449dbf97188df5&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%228CB9973E-7241-4F21-9F54-9F1C32855215.jpeg%22&x-id=GetObject"
        alt="happy developers"
        style="width: 200px"
      />
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