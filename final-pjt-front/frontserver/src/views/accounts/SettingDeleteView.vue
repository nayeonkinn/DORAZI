<template>
	<div>
		<h1>delete account</h1>
		<p>탈퇴 후에는 계정을 복구할 수 없습니다.</p>
		<p>탈퇴를 원하시는 경우 유저네임을 입력해 주세요.</p>
		<p>{{ username }}</p>
		<form @submit.prevent="deleteAccount">
			<input v-model="input"/>
			<button>탈퇴</button>
		</form>
	</div>
</template>

<script>
export default {
	name: 'SettingDeleteView',
	data() {
		return {
      input: null,
    }
	},
	computed: {
		username() {
			return this.$store.state.username
		}
	},
	methods: {
		deleteAccount() {
			if (this.username == this.input) {
				this.$store.dispatch('deleteAccount')
				this.$router.push({ name: 'MainView' })
			} else {
				alert('유저네임을 올바르게 입력해 주세요.')
			}
    }
	}
}
</script>

<style>

</style>