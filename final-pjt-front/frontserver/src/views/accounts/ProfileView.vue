<template>
  <div class="container">
    <div class="d-flex justify-content-center align-items-center">
      <div>
        <span class="logoFont" style="font-size: 100px">{{ yourName }}</span>
      </div>
      <div v-if="myName != yourName">
        <svg
          @click="follow"
          id="likeBtn"
          xmlns="http://www.w3.org/2000/svg"
          width="50"
          height="50"
          fill="currentColor"
          class="bi bi-heart-fill cursorPointer"
          viewBox="0 0 16 16"
          :class="[isFollowed ? 'likeColor' : 'notLikeColor']"
          style="margin-left: 10px"
        >
          <path
            fill-rule="evenodd"
            d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"
          />
        </svg>
      </div>
    </div>

    <div class="d-flex justify-content-around my-4">
      <div>
        <span>{{ articles_count }}</span>
        <p>posts</p>
      </div>
      <div>
        <span>{{ wishes_count }}</span>
        <p>wishes</p>
      </div>
      <div>
        <span>{{ followers_count }}</span>
        <p>followers</p>
      </div>
      <div>
        <span>{{ followings_count }}</span>
        <p>followings</p>
      </div>
    </div>
    <ProfileArticleList :articles_list="articles_list" :yourName="yourName" />
    <ProfileWishList :wishes_list="wishes_list" :yourName="yourName" />
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
    token() {
      return this.$store.state.token;
    },
  },
  methods: {
    getProfile() {
      axios({
        method: "get",
        url: `${API_URL}/profile/${this.yourName}/`,
        headers: {
          Authorization: `Token ${this.token}`,
        },
      })
        .then((response) => {
          // console.log(response)
          const followers = response.data.followers;
          this.isFollowed = followers.includes(this.myId);

          this.articles_count = response.data.articles_count;
          this.wishes_count = response.data.wishes_count;
          this.followers_count = response.data.followers_count;
          this.followings_count = response.data.followings_count;

          this.articles_list = response.data.articles_list;
          this.wishes_list = response.data.wishes_list;
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
          Authorization: `Token ${this.token}`,
        },
      })
        .then((response) => {
          // console.log(response)
          this.isFollowed = response.data.is_followed;
          this.followers_count = response.data.followers_count;
          this.followings_count = response.data.followings_count;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getProfile();
  },
  watch: {
    "$route.params": function () {
      this.getProfile();
    },
  },
  // updated() {
  //   this.getProfile()
  // },
};
</script>

<style>
</style>