import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

Vue.use(IconsPlugin)
Vue.use(BootstrapVue)
Vue.config.productionTip = false
Vue.config.ignoredElements = [/^ion-/]


new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
