<template>
	<div class="card text-bg-dark">
		<img :src="poster_path" alt="poster_img" style="width: 300px; height: 400px;">
		<div class="card-img-overlay">
			<h5 class="card-title">{{ movie_title }}</h5>
			<p class="card-text"><small>{{ movie_release_date }}</small></p>
		</div>
	</div>
</template>

<script>
export default {
	name: 'ProfileArticleItem',
	props: {
		article: Object,
	},
	computed: {
		poster_path() {
			return "https://image.tmdb.org/t/p/original/" + this.article.movie.poster_path
		},
		movie_title() {
			return this.article.movie.title
		},
		movie_release_date() {
			return this.article.movie.release_date.substr(0, 4)
		}
	}
}
</script>

<style>

</style>