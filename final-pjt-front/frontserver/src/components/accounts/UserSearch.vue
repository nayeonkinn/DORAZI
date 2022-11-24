<template>
  <div>
    <router-link
      style="text-decoration: none; color: white; font-size: 40px"
      class="logoFont"
      :to="{ name: 'ProfileView', params: { username: username } }"
    >
      <span id="userResult">
        {{ username }}
      </span>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "UserSearch",
  props: {
    user: Object,
  },
  data() {
    return {
      username: this.user.username,
    };
  },
  computed: {},
};
</script>

<style>
#userResult:hover {
  color: rgb(255, 200, 47);
}
</style>