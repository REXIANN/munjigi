import cookies from "vue-cookies";
import router from "../routes";
export default {
  ADD_COUNT(state) {
    state.count++;
  },
  SET_TOKEN(state, token) {
    state.authToken = token;
    cookies.set("auth-token", token);
  },
  SELECT_REVIEW(state, review) {
    state.review = review;
    router.push({ name: "CommunityReviewItem", params: { id: review.id } });
  },
  SET_USER_DATA(state, user) {
    const userData = {
      // res.user informations
      birth: user.birth,
      dateJoined: user.date_joined,
      email: user.email,
      id: user.id,
      name: user.name,
      nickname: user.nickname,
    };
    state.userData = userData;
  },
};
