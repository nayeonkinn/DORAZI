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
import MovieView from '@/views/movies/MovieView'
import MovieDetailView from '@/views/movies/MovieDetailView'

// search
import SearchView from '@/views/search/SearchView'

Vue.use(VueRouter)


const routes = [
  {
    path: '/',
    name: 'MainView',
    component: MainView,
  },
  {
    path: '/accounts/signup/',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/accounts/login/',
    name: 'LoginView',
    component: LoginView,
    beforeEnter(to, from, next) {
      // console.log('beforeEnter: ', from.name, ' -> ', to.name)
      // console.log('isLoggedIn: ', store.getters.isLogin)
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
    path: '/accounts/profile/:username/',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/movies/',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/movies/:movie_pk',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/search/:q',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/articles/:article_id/',
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
  const authPages = ['MainView']
  const isAuthRequired = authPages.includes(to.name)
  
  // console.log('beforeEach: ', from.name, ' -> ', to.name)
  // console.log('loginRequired: ', isAuthRequired, ' isLoggedIn: ', isLoggedIn)
  if (isAuthRequired && !isLoggedIn) {
    next({ name: 'LoginView' })
  } else if (to != from) {
    next()
  }
})

export default router
