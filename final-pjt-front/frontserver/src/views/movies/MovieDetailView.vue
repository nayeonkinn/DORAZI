<template>
  <div>
    <moviedetail/>
  </div>
</template>

<script>
import moviedetail from "@/components/movies/MovieDetail.vue";


export default {
  components: {
    moviedetail,
  },
  name: "MovieDetailView",
};
</script>


<style>
.single {
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  height: 300px;
  border: 2px solid;
}
</style>