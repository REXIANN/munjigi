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
};
