import Vue from 'vue'
import Vuex from 'vuex'
import getters from './getters'
import actions from './actions'
import mutations from './mutations'
// Promise imported for various browsers
import 'es6-promise/auto'

Vue.use(Vuex)

const state = {
  test: 'hello world',
}

export default new Vuex.Store({
  state,
  mutations,
  getters,
  actions
})
