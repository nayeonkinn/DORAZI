<template>
  <div>
    <h3>RECOMMEND POPULAR USERS</h3>
    <RecoFriendsItem
      v-for="friend in friends"
      :key="`user-${friend.id}`"
      :friend="friend"
    ></RecoFriendsItem>
  </div>
</template>

<script>
import axios from "axios";
import RecoFriendsItem from "@/components/articles/RecoFriendsItem";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "RecoFriendsList",
  components: {
    RecoFriendsItem,
  },
  data() {
    return {
      friends: null,
    };
  },
  computed: {
    token() {
      return this.$store.state.token;
    },
  },
  methods: {
    getFriends() {
      axios({
        method: "get",
        url: `${API_URL}/articles/recommend/friends/`,
        headers: {
          Authorization: `Token ${this.token}`,
        },
      })
        .then((response) => {
          // console.log(response);
          this.friends = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getFriends();
  },
};
</script>

<style>
</style>