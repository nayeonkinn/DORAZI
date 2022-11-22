<template>
  <div>
    <h1>Signup</h1>
    <form @submit.prevent="signup">
      <label for="username">username : </label>
      <input type="text" id="username" v-model.trim="username" />

      <label for="password1">password : </label>
      <input type="password" id="password1" v-model.trim="password1" />

      <label for="password2">password confirmation : </label>
      <input type="password" id="password2" v-model.trim="password2" />

      <input type="submit" value="Signup" />
    </form>
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
</style>