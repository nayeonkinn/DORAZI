<template>
  <div>
    <h1>{{ yourName }}</h1>
    <form v-if="myName != yourName" @submit.prevent="follow">
      <button>{{ followMsg }}</button>
    </form>
    <div>
      <p>{{ articles_count }} posts</p>
      <p>{{ wishes_count }} wishes</p>
      <p>{{ followers_count }} followers</p>
      <p>{{ followings_count }} followings</p>
    </div>
    <ProfileArticleList :articles_list="articles_list"/>
    <ProfileWishList :wishes_list="wishes_list"/>
  </div>
</template>

<script>
import ProfileArticleList from "@/components/accounts/ProfileArticleList";
import ProfileWishList from "@/components/accounts/ProfileWishList";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "ProfileView",
  components: {
    ProfileArticleList,
    ProfileWishList,
  },
  data() {
    return {
      isFollowed: null,
      articles_count: null,
      wishes_count: null,
      followers_count: null,
      followings_count: null,
      articles_list: null,
      wishes_list: null,
    };
  },
  computed: {
    myName() {
      return this.$store.state.username;
    },
    myId() {
      return this.$store.state.userId;
    },
    yourName() {
      return this.$route.params.username;
    },
    followMsg() {
      return this.isFollowed ? "Unfollow" : "Follow"
    },
    token() {
      return this.$store.state.token;
    }
  },
  methods: {
    getProfile() {
      axios({
        method: "get",
        url: `${API_URL}/profile/${this.yourName}/`,
      })
        .then((response) => {
          // console.log(response)
          const followers = response.data.followers;
          this.isFollowed = followers.includes(this.myId);

          this.articles_count = response.data.articles_count
          this.wishes_count = response.data.wishes_count
          this.followers_count = response.data.followers_count;
          this.followings_count = response.data.followings_count;

          this.articles_list = response.data.articles_list
          this.wishes_list = response.data.wishes_list
        })
        .catch((error) => {
          console.log(error);
        });
      },
      follow() {
        axios({
          method: "post",
          url: `${API_URL}/profile/${this.yourName}/follow/`,
          headers: {
            Authorization: `Token ${this.token}`
          }
        })
        .then((response) => {
          // console.log(response)
          this.isFollowed = response.data.is_followed
          this.followers_count = response.data.followers_count;
          this.followings_count = response.data.followings_count;
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created() {
    this.getProfile();
  },
  watch: {
    '$route.params': function() {
      this.getProfile();
    },
  }
  // updated() {
  //   this.getProfile()
  // },
};
</script>

<style>
</style>