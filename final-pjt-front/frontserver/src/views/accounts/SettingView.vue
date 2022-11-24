<template>
  <div class="container">
    <h1 class="mb-5" style="margin-top: 100px">설정</h1>
    <nav>
      <div>
        <router-link
          style="text-decoration: none; color: black"
          :to="{ name: 'SettingPasswordView' }"
        >
          <button id="userBtn">비밀번호 변경</button>
        </router-link>
      </div>
      <div>
        <router-link
          style="text-decoration: none; color: black"
          :to="{ name: 'SettingDeleteView' }"
        >
          <button id="userBtn">회원 탈퇴</button>
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
#userBtn {
  width: 230px;
  height: 70px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: 700;
  color: #000;
  background-color: rgb(255, 255, 255);
  border: none;
  border-radius: 40px;
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease 0s;
  cursor: pointer;
  outline: none;
  margin-bottom: 30px;
}

#userBtn:hover {
  background-color: rgb(151, 151, 151);
  box-shadow: 0px 15px 20px rgba(158, 158, 158, 0.15);
  color: #fff;
}
</style>