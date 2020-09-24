export default {
  count: 0,
  authToken: sessionStorage.getItem("auth-token") === "undefined"? null: sessionStorage.getItem("auth-token"),
  selectedKeyword: "",
  review: {
    type: Object,
  },
  heritage: {
    type: Object,
  },
};
