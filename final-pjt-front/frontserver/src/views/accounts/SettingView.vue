<template>
  <div>
    <h1>Setting</h1>
    <nav>
      <router-link :to="{ name: 'SettingPasswordView' }">Change Password</router-link><br>
      <router-link :to="{ name: 'SettingDeleteView' }">Delete Account</router-link>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'SettingView',
}
</script>

<style>

</style>