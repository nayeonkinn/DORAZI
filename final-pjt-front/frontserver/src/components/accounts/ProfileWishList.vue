<template>
  <div>
    <section class="movies">
      <h1>보고 싶어하는 영화</h1>
      <div class="movies-grid">
        <ProfileWishItem
          v-for="wish in wishes_list"
          :key="`movie-${wish.id}`"
          :wish="wish"
          class="col"
        />
      </div>
      <hr />
    </section>
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
};
</script>

<style>
</style>