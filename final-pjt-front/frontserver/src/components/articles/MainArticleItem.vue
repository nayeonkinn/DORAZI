<template>
	<div>
		<p>{{article}}</p>
		<img :src="poster_path" alt="poster_img" style="width: 200px; height: 300px;">
		<h3>{{ article.user.username }}</h3>
		<p>{{ article_created_at }}</p>
		<p>{{ article.rating }}</p>
		<p>{{ article.content }}</p>
		<p>좋아요 {{ article.like_users.length }}</p>
		<p>댓글 {{ article.articlecomment_set.length }}</p>
		<hr>
	</div>
</template>

<script>
import moment from 'moment'

export default {
	name: 'MainArticleItem',
	props: {
		article: Object,
	},
	computed: {
		article_created_at() {
			return moment(String(this.article.created_at)).format('YYYY-MM-DD HH:mm')
		},
		poster_path() {
			return "https://image.tmdb.org/t/p/original/" + this.article.movie.poster_path
		},
	}
}
</script>

<style>

</style>