<template>
	<div>
		<h1>후기를 남긴 영화</h1>
		<div class="row row-cols-1 row-cols-md-3 g-4">
			<ProfileArticleItem
			v-for="article in articles_list"
			:key="`article-${article.id}`"
      :article="article"
			class="col"
			/>
		</div>
	</div>
</template>

<script>
import ProfileArticleItem from '@/components/accounts/ProfileArticleItem'

export default {
	name: 'ProfileArticleList',
	components: {
		ProfileArticleItem
	},
	props: {
		articles_list: Array,
	}
}
</script>

<style>

</style>