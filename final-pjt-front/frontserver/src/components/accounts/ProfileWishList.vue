<template>
  <div>
    <section class="movies">
      <p class="profileTitle">{{ yourName }}님이 보고 싶어하는 영화</p>
      <div v-if="wishes_list?.length" class="movies-grid">
        <ProfileWishItem
          v-for="wish in wishes_list"
          :key="`movie-${wish.id}`"
          :wish="wish"
          class="col"
        />
      </div>
      <div v-else style="margin: 100px 0px;">
        <p>앗.. 아직 없어요!</p>
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
    yourName: String,
  },
};
</script>

<style>
</style>