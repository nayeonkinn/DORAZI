import Vue from 'vue'
import VueRouter from 'vue-router'

import HomeView from '@/views/HomeView'

// accounts
import SignupView from '@/views/accounts/SignupView'
import LoginView from '@/views/accounts/LoginView'
import SettingView from '@/views/accounts/SettingView'
import SettingPasswordView from '@/views/accounts/SettingPasswordView'
import ProfileView from '@/views/accounts/ProfileView'

// movies
import MovieView from '@/views/movies/MovieView'
import MovieDetailView from '@/views/movies/MovieDetailView' 

// article
import ArticleCreateView from '@/views/articles/ArticleCreateView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/accounts/signup/',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/accounts/login/',
    name: 'LoginView',
    component: LoginView
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
    path: '/arcitle/create/:movie_pk',
    name: 'ArticleCreateView',
    component: ArticleCreateView

  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
