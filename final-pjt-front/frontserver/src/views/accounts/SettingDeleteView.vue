<template>
  <div class="container">
    <h1 class="mb-5" style="margin-top: 100px">회원 탈퇴</h1>

    <span
      class="mb-5"
      style="margin-top: 100px; line-height: 170%; font-size: 20px"
    >
      탈퇴 후에는 계정을 복구할 수 없습니다.<br />탈퇴를 원하시는 경우
      유저네임을 동일하게 입력해 주세요.
    </span>

    <div id="idExample" class="deleteBox">
      <span>{{ username }}</span>
    </div>

    <form @submit.prevent="deleteAccount" class="my-3">
      <div>
        <input id="idInput" class="deleteBox" v-model="input" />
      </div>
      <button class="deleteBtn">탈퇴하겠습니다.</button>
    </form>
    <p style="font-size: 18px">
      <router-link class="linkGray" :to="{ name: 'SettingView' }"
        >탈퇴하지 않고 뒤로가기</router-link
      >
    </p>
  </div>
</template>

<script>
export default {
  name: "SettingDeleteView",
  data() {
    return {
      input: null,
    };
  },
  computed: {
    username() {
      return this.$store.state.username;
    },
  },
  methods: {
    deleteAccount() {
      if (this.username == this.input) {
        this.$store.dispatch("deleteAccount");
        this.$router.push({ name: "MainView" });
      } else {
        alert("유저네임을 올바르게 입력해 주세요.");
      }
    },
  },
};
</script>

<style>
</style>
