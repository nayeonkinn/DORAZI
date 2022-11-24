<template>
  <div>
    <section class="movies">
      <p class="profileTitle">{{ username }}님이 보고 싶어하는 영화</p>
      <div class="movies-grid">
        <ProfileWishItem
          v-for="wish in wishes_list"
          :key="`movie-${wish.id}`"
          :wish="wish"
          class="col"
        />
      </div>
    </section><br>
  </div>
</template>

<script>
import ProfileWishItem from "@/components/accounts/ProfileWishItem";

export default {
  name: "ProfileWishList",
  components: {
    ProfileWishItem,
  },
  props: {
    wishes_list: Array,
  },
  computed: {
    username() {
      return this.$store.state.username;
    },
  },
};
</script>

<style>
</style>