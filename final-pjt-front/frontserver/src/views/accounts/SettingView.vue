<template>
  <div class="container">
    <h1 class="mb-5" style="margin-top: 100px">설정</h1>
    <nav>
      <div>
        <router-link
          style="text-decoration: none; color: black"
          :to="{ name: 'SettingPasswordView' }"
        >
          <button id="settingUserBtn">비밀번호 변경</button>
        </router-link>
      </div>
      <div>
        <router-link
          style="text-decoration: none; color: black"
          :to="{ name: 'SettingDeleteView' }"
        >
          <button id="settingUserBtn">회원 탈퇴</button>
        </router-link>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "SettingView",
};
</script>

<style>
</style>