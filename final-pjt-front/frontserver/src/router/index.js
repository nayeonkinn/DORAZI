import Vue from 'vue'
import VueRouter from 'vue-router'

import store from '@/store/index.js'

// accounts
import SignupView from '@/views/accounts/SignupView'
import LoginView from '@/views/accounts/LoginView'
import SettingView from '@/views/accounts/SettingView'
import SettingPasswordView from '@/views/accounts/SettingPasswordView'
import SettingDeleteView from '@/views/accounts/SettingDeleteView'
import ProfileView from '@/views/accounts/ProfileView'

// article
import MainView from '@/views/articles/MainView'
import ArticleDetailView from '@/views/articles/ArticleDetailView'

// movies
import ReccomendView from '@/views/movies/ReccomendView'
import MovieDetailView from '@/views/movies/MovieDetailView'

// search
import SearchView from '@/views/search/SearchView'
import SearchResultView from '@/views/search/SearchResultView'

Vue.use(VueRouter)


const routes = [
  {
    path: '/main',
    name: 'MainView',
    component: MainView,
  },
  {
    path: '/accounts/signup',
    name: 'SignupView',
    component: SignupView,
    beforeEnter(to, from, next) {
      if (store.getters.isLogin) {
        next({ name: 'MainView' })
      } else {
        next()
      }
    }
  },
  {
    path: '/accounts/login',
    name: 'LoginView',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (store.getters.isLogin) {
        next({ name: 'MainView' })
      } else {
        next()
      }
    }
  },
  {
    path: '/accounts/setting',
    name: 'SettingView',
    component: SettingView
  },
  {
    path: '/accounts/setting/password',
    name: 'SettingPasswordView',
    component: SettingPasswordView
  },
  {
    path: '/accounts/setting/delete',
    name: 'SettingDeleteView',
    component: SettingDeleteView
  },
  {
    path: '/accounts/profile/:username',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/movies/',
    name: 'ReccomendView',
    component: ReccomendView
  },
  {
    path: '/movies/:movie_pk',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/search',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/search/:q',
    name: 'SearchResultView',
    component: SearchResultView
  },
  {
    path: '/articles/:article_id',
    name: 'ArticleDetailView',
    component: ArticleDetailView
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const isLoggedIn = store.getters.isLogin
  const allowedPaged = ['SignupView', 'LoginView']
  const isAuthRequired = !allowedPaged.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    next({ name: 'LoginView' })
  } else if (to != from) {
    next()
  }

  const searchPages = ['SearchView', 'SearchResultView']
  const isFromSearch = searchPages.includes(from.name)
  const isToSearch = searchPages.includes(to.name)

  if (isFromSearch && !isToSearch) {
    store.state.q = null
    store.state.resultOn = false
  }
})

export default router
