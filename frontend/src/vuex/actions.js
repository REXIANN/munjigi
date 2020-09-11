export default {
  login({ state, commit }, loginData) {
    console.log(loginData);
    console.log(state, commit);
    
  },
  signup({ state, commit }, signupData) {
    console.log(signupData);
    console.log(state, commit);
  },
};
