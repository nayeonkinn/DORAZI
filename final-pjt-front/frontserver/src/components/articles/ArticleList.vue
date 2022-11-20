<template>
  <div>
    <router-link :to="{ name: 'ProfileView', params: {'username': writer }}" >
      <h3>{{ writer }}</h3>
    </router-link>
    <h4>{{ content }}</h4>
    <div> {{ updatedate }}</div>
    <div> {{ likenum }}</div>
    <form v-if="now" @submit.prevent="sending" @exit.prevent="update">
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="articlecontent"></textarea><br>
      <input type="submit" id="submit">
    </form>
    <button @click="update" > 수정하기 </button>
    <button @click="Delete" > 삭제하기 </button>
  </div>

</template>

<script>
import  axios from 'axios'
const API_URL = "http://127.0.0.1:8000";

export default {
name:'ArticleList',
props:{
  article: Object,
},
data() { 
  return {
    now: false,
    articlecontent: null,
  }
},
computed: {
    writer() {
      return this.article.user.username },
    updatedate() {
      return this.article.updated_at.slice(0,10) },
    spoiler () {
      return this.article.spoiler},
    likenum() {
      return this.article.like_users.lenght},
    content() {
      return this.article.content },

  },
  methods: {
    update() {
      this.articlecontent = this.content
      this.now = !this.now
    },
    sending(){
      const title = this.articletitle;
      const content = this.articlecontent;
      if (!content) {
        alert("내용을 입력해주세요");
        return;
      }
      console.log(content)
      axios({
        method: "PUT",
        url: `${API_URL}/articles/${this.article.id}/`,
        data: {
          title: title,
          content: content,
          spoiler: false,
          rating: 5,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          this.update()
          this.$emit('update', this.article);

        })
        .catch((err) => {
          console.log(err);
        });
    },
    Delete() {
      axios({
        method: "DELETE",
        url: `${API_URL}/articles/${this.article.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          this.update()
          this.$emit('update');

        })
        .catch((err) => {
          console.log(err);
        });
      this.$emit('update', this.article);}
    }
  }

</script>

<style>

</style>