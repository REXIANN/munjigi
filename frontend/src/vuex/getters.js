export default {
  isLogin: state => !!state.auth_token,
  config: state => ({ headers: { Authorization: `Token ${state.authToken}` } }) 
}