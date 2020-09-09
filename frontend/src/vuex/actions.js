export default {
  login({ state, commit }, loginData) {
    console.log(loginData);
    console.log(state, commit);
    // axios
    //   .post(address, loginData, header)
    //   .then()
    //   .catch()
    //   .finaly();
  },
  signup({ state, commit }, signupData) {
    console.log(signupData);
    console.log(state, commit);
  },
};
