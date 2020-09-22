import router from "../routes";
export default {
  ADD_COUNT(state) {
    state.count++;
  },
  SET_TOKEN(state, token) {
    state.authToken = token;
  },
  SELECT_REVIEW(state, review) {
    state.review = review;
    router.push({ name: "CommunityReviewItem", params: { id: review.id } });
  },
  SELECT_HERITAGE(state, heritage) {
    state.heritage = heritage;
    router.push({ name: "HeritageCardDetail", params: { id: heritage.id } });
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
