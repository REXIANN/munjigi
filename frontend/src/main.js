import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
// Add vue router
import VueRouter from 'vue-router'
import routes from './routes.js'
// Add vuex
import store from './vuex/store'

Vue.config.productionTip = false

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

new Vue({
  store,
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
