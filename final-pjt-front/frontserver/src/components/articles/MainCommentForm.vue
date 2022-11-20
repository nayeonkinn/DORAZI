<template>
	<div>
		<textarea v-model="comment" @keyup.enter="createComment" cols="40" rows="1"></textarea>
		<button type='button' @click="createComment">등록</button>
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