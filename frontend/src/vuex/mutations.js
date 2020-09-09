export default {
  ADD_COUNT(state) {
    state.count++;
  },
  // 로그인 관련 함수
  LOGIN(state) {
    console.log(state.loginData);
    // router.push({ name: "Home" });
  },
  UPDATE_NICKNAME(state, value) {
    state.loginData.nickname = value;
  },
  UPDATE_PASSWORD(state, value) {
    state.loginData.password = value;
  },
};
