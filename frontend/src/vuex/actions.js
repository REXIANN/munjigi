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
  checkEmail({ state, commit }, email) {
    console.log(email);
    console.log(state, commit);
  },
  checkPassword({ state, commit }, password) {
    console.log(password);
    console.log(state, commit);
  },
};
