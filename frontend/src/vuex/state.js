import cookies from "vue-cookies";

export default {
  count: 0,
  authToken: cookies.get("auth-token"),
  userData: {
    nickname: "",
    id: "",
    email: "",
  },
  review: {
    type: Object,
  },
  heritage: {
    type: Object,
  },
};
