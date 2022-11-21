<template>
	<div>
		<form @submit.prevent="createComment">
			<input v-model="comment" cols="40" rows="1"/>
			<button>등록</button>
		</form>
	</div>
</template>

<script>
import axios from 'axios';

const API_URL = "http://127.0.0.1:8000";

export default {
	name: 'MainCommentForm',
	props: {
		articleId: Number,
	},
	data() {
    return {
      comment: null,
    }
	},
	computed: {
		token() {
			return this.$store.state.token;
		}
	},
	methods: {
		createComment() {
      axios({
				method: 'POST',
				url: `${API_URL}/articles/${this.articleId}/comment_create/`,
				headers: {
          Authorization: `Token ${this.token}`,
        },
				data: {
					content: this.comment,
				}
			})
				.then((response) => {
					// console.log(response)
					this.$emit('create-comment', response.data)
				})
				.catch((error) => {
          console.log(error)
				})

			this.comment = null
		}
	}
}
</script>

<style>

</style>