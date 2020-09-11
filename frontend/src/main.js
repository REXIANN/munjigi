import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
// Add vue router
import VueRouter from 'vue-router'
import routes from './routes'
// Add vuex
import store from './vuex/index'

// Add vue-cookies
import VueCookies from 'vue-cookies'

Vue.config.productionTip = false

Vue.use(VueCookies)
Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

new Vue({
  store,
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
