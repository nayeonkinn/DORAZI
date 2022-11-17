import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import SignupView from '@/views/SignupView'
import LoginView from '@/views/LoginView'
import UserUpdateView from '@/views/UserUpdateView'
import ProfileView from '@/views/ProfileView'

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
    path: '/accounts/settings/',
    name: 'UserUpdateView',
    component: UserUpdateView,
    // children: {
    // }
  },
  {
    path: '/accounts/profile/:username/',
    name: 'ProfileView',
    component: ProfileView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
