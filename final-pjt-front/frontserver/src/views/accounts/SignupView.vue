<template>
  <div class="container">
    <h1 class="mb-5" style="margin-top: 250px; line-height: 170%">
      <span class="logoFont">cinema.log</span>에 가입하고<br />친구들과 영화로
      대화를 나눠 보세요
    </h1>
    <div class="d-flex justify-content-center align-items-center">
      <div id="signupForm" style="width: 500px">
        <form @submit.prevent="signup" class="mb-5">
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
          <div class="form-floating mb-3">
            <input
              v-model.trim="password1"
              type="password"
              class="form-control"
              id="floatingPassword"
              placeholder="비밀번호"
            />
            <label for="floatingPassword">비밀번호</label>
          </div>
          <div class="form-floating mb-4">
            <input
              v-model.trim="password2"
              type="password"
              class="form-control"
              id="floatingPassword"
              placeholder="비밀번호 확인"
            />
            <label for="floatingPassword">비밀번호 확인</label>
          </div>
          <div class="d-grid gap-2 mb-4">
            <button id="signupBtn" class="btn">회원가입</button>
          </div>
        </form>
        <p style="font-size: 18px">
          계정이 이미 있으신가요?
          <router-link id="toLogin" :to="{ name: 'LoginView' }"
            >로그인</router-link
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignupView",
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    };
  },
  methods: {
    signup() {
      if (!this.username) {
        alert("아이디를 입력해 주세요.");
        return;
      } else if (!this.password1) {
        alert("비밀번호를 입력해 주세요.");
        return;
      } else if (!this.password2) {
        alert("비밀번호 확인을 입력해 주세요.");
        return;
      }

      const payload = {
        username: this.username,
        password1: this.password1,
        password2: this.password2,
      };
      this.$store.dispatch("signup", payload);

      this.username = null;
      this.password1 = null;
      this.password2 = null;

      // this.$router.push({ name: 'MainView' }).catch(() => {})
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Crimson+Text:wght@700&family=Gothic+A1&family=Noto+Sans+KR&display=swap");

.logoFont {
  font-family: "Crimson Text", serif;
  font-size: 50px;
  /* color: rgb(255, 200, 47) */
}

#signupBtn {
  height: 58px;
  color: white;
  background-color: rgb(53, 53, 53);
  z-index: 1;
}

#toLogin {
  color: rgb(158, 158, 158);
  text-decoration: none;
}
</style>