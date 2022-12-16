<template>
  <div class="container">
    <h1 class="mb-5" style="margin-top: 100px">
      비밀번호 변경
    </h1>

    <div class="d-flex justify-content-center align-items-center">
      <div style="width: 500px">
        <form @submit.prevent="changePassword" class="mb-5">
          <div class="form-floating mb-3">
            <input
              v-model.trim="old_password"
              type="password"
              class="form-control"
              id="floatingInput"
              placeholder="현재 비밀번호"
            />
            <label for="floatingInput">현재 비밀번호</label>
          </div>
          <div class="form-floating mb-3">
            <input
              v-model.trim="new_password1"
              type="password"
              class="form-control"
              id="floatingPassword1"
              placeholder="새 비밀번호"
            />
            <label for="floatingPassword1">새 비밀번호</label>
          </div>
          <div class="form-floating mb-4">
            <input
              v-model.trim="new_password2"
              type="password"
              class="form-control"
              id="floatingPassword2"
              placeholder="새 비밀번호 확인"
            />
            <label for="floatingPassword2">새 비밀번호 확인</label>
          </div>
          <div class="d-grid gap-2 mb-4">
            <button id="submitBtn" class="btn">변경</button>
          </div>
        </form>
        <p style="font-size: 18px">
          <router-link class="linkGray" :to="{ name: 'SettingView' }"
            >뒤로가기</router-link
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SettingPasswordView',
  data() {
    return {
      old_password: null,
      new_password1: null,
      new_password2: null,
    }
  },
  methods: {
    changePassword() {
      if (!this.old_password) {
        alert("현재 비밀번호를 입력해 주세요.");
        return;
      } else if (!this.new_password1) {
        alert("새 비밀번호를 입력해 주세요.");
        return;
      } else if (!this.new_password2) {
        alert("새 비밀번호 확인을 입력해 주세요.");
        return;
      }

      const old_password = this.old_password
      const new_password1 = this.new_password1
      const new_password2 = this.new_password2

      const payload = {
        old_password: old_password,
        new_password1: new_password1,
        new_password2: new_password2,
      }
      this.$store.dispatch('changePassword', payload)
    }
  }
}
</script>

<style>
</style>