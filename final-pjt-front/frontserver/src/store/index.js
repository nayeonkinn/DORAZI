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
    LOGOUT(state) {
      state.token = null
      localStorage.removeItem('token')
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
        .catch((error) => {
          console.log(error)
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
          context.commit('LOGOUT')
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
    }
  },
  modules: {
  }
})
