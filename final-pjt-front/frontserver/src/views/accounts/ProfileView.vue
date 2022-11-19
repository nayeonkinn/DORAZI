<template>
  <div>
    <h1>{{ username }}</h1>
  </div>
</template>

<script>
export default {
  name: 'ProfileView',
  computed: {
    username() {
      return this.$store.state.username
    }
  },
  methods: {
  },
}
</script>

<style>

</style>