import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: null,
    userId: null,
    username: null,
    search: null,
    articledetail: null,
    resultOn: false,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
    },
    SAVE_USER_INFO(state, userData) {
      state.userId = userData.pk
      state.username = userData.username
    },
    DELETE_USER_INFO(state) {
      state.token = null
      state.userId = null
      state.username = null
      localStorage.removeItem('token')
    },
    SEARCH(state, q) {
      state.search = null
      state.search = q
      state.resultOn = true
    }
  },
  actions: {
    signup(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((response) => {
          context.commit('SAVE_TOKEN', response.data.key)
        })
        .then(() => {
          this.dispatch('save_user_info')
        })
        .catch((error) => {
          // console.log(error)
          const errors = error.response.data
          const firstError = Object.values(errors)[0][0]
          alert(firstError)
        })
      },
      login(context, payload) {
        axios({
          method: 'post',
          url: `${API_URL}/accounts/login/`,
          data: {
            username: payload.username,
            password: payload.password,
          }
        })
        .then((response) => {
          context.commit('SAVE_TOKEN', response.data.key)
        })
        .then(() => {
          this.dispatch('save_user_info')
        })
        .catch((error) => {
          console.log(error)
          alert('아이디 또는 비밀번호가 올바르지 않습니다.')
        })
      },
      save_user_info(context) {
        axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
      .then((response) => {
        context.commit('SAVE_USER_INFO', response.data)
        window.location.reload(true)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    logout(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
      })
        .then(() => {
          context.commit('DELETE_USER_INFO')
          window.location.reload(true)
        })
        .catch((error) => {
          console.log(error)
        })
      },
      changePassword(context, payload) {
        axios({
          method: 'post',
          url: `${API_URL}/accounts/password/change/`,
          data: {
            new_password1: payload.new_password1,
            new_password2: payload.new_password2,
            old_password: payload.old_password,
          },
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
      .catch((error) => {
        console.log(error)
      })
    },
    deleteAccount(context) {
      axios({
        method: 'delete',
        url: `${API_URL}/profile/delete/`,
        headers: {
          Authorization: `Token ${this.state.token}`
        }
      })
      .then(() => {
        context.commit('DELETE_USER_INFO')
        window.location.reload(true)
      })
      .catch((error) => {
        console.log(error)
      })
    },
  },
  modules: {
  }
})
