<template>
  <div>
    <router-link :to="{ name: 'ProfileView', params: {'username': username }}">
    {{ username }}
    </router-link>
  </div>
</template>

<script>
export default {
 name:'UserSearch',
 props:{
  user:Object
 },
 data() {
  return {
    username:this.user.username
  }
 },
 computed: {

 }
}
</script>

<style>

</style>