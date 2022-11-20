<template>
    <div>
      <router-link :to="{ name: 'ProfileView', params: {'username': writer }}" >
        <h3>{{ writer }}</h3>
      </router-link>
      <h4>{{ content }}</h4>
      <div> {{ updatedate }}</div>
      <div> {{ likenum }}</div>
    </div>
  
  </template>
  
  <script>
  
  export default {
  name:'ArticleSimple',
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

    }}
  
  </script>
  
  <style>
  
  </style>