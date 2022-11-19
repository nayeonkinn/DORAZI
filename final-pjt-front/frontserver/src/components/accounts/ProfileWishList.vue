<template>
	<div>
		<h1>보고 싶어하는 영화</h1>
		<div class="row row-cols-1 row-cols-md-3 g-4">
			<ProfileWishItem
			v-for="wish in wishes_list"
			:key="`movie-${wish.id}`"
      :wish="wish"
			class="col"
			/>
		</div>
	</div>
</template>

<script>
import ProfileWishItem from '@/components/accounts/ProfileWishItem'

export default {
	name: 'ProfileWishList',
	components: {
		ProfileWishItem
	},
	props: {
		wishes_list: Array,
	}
}
</script>

<style>

</style>