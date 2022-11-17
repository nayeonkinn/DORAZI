<template>
  <div>
    <h1>Change Password</h1>
    <form @submit.prevent="changePassword">
      <label for="old_password">old password : </label>
      <input type="password" id="old_password" v-model="old_password">

      <label for="new_password1">new password : </label>
      <input type="password" id="new_password1" v-model="new_password1">

      <label for="new_password2">new password confirmation : </label>
      <input type="password" id="new_password2" v-model="new_password2">

      <input type="submit" value="Submit">
    </form>
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
      const old_password = this.old_password
      const new_password1 = this.new_password1
      const new_password2 = this.new_password2

      const payload = {
        old_password: old_password,
        new_password1: new_password1,
        new_password2: new_password2,
      }
      this.$store.dispatch('changePassword', payload)
      this.$router.push({ name: 'SettingView'})
    }
  }
}
</script>

<style>

</style>