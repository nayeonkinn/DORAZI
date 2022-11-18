import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import SignupView from '@/views/SignupView'
import LoginView from '@/views/LoginView'
import SettingView from '@/views/SettingView'
import SettingPasswordView from '@/views/SettingPasswordView'
import ProfileView from '@/views/ProfileView'
import MovieDetailView from '@/views/MovieDetailView' 

// Movies
import MovieView from '@/views/MovieView'


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
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
