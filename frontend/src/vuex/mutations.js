import cookies from 'vue-cookies'
export default {
  ADD_COUNT(state) {
    state.count++;
  },
  SET_TOKEN(state, token) {
    state.authToken = token
    cookies.set('auth-token', token)
  },
};
