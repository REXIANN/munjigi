import axios from "axios"
import cookies from "vue-cookies"
import router from "@/routes"
import SERVER from "@/api/drf"

export default {
  postAuthData({ commit }, info) {
    axios
      .post(info.location, info.data)
      .then((res) => {
        commit("SET_TOKEN", res.data.token)
        cookies.set("auth-token", res.data.token, 0)
        // sessionStorage에 유저의 정보를 저장
        sessionStorage.setItem("birth", res.data.user.birth)
        sessionStorage.setItem("dateJoined", res.data.user.date_joined)
        sessionStorage.setItem("email", res.data.user.email)
        sessionStorage.setItem("id", res.data.user.id)
        sessionStorage.setItem("name", res.data.user.name)

        router.push({ name: "Home" })
      })
      .catch((err) => {
        console.log(err.message)
      })
  },
  signup({ dispatch }, signupData) {
    const info = {
      location: SERVER.URL + SERVER.ROUTES.signup,
      data: signupData,
    }
    dispatch("postAuthData", info)
  },
  login({ dispatch }, loginData) {
    const info = {
      location: SERVER.URL + SERVER.ROUTES.login,
      data: loginData,
    }
    dispatch("postAuthData", info)
  },

  logout({ getters, commit }) {
    axios
      .post(SERVER.URL + SERVER.ROUTES.logout, null, getters.config)
      .then(() => {
        commit("SET_TOKEN", null)
        cookies.remove("auth-token")
        // 세션에 있는 정보를 지움
        sessionStorage.removeItem("birth")
        sessionStorage.removeItem("dateJoined")
        sessionStorage.removeItem("email")
        sessionStorage.removeItem("id")
        sessionStorage.removeItem("name")
      })
      .catch((err) => {
        console.log(err.message)
      })
  },
}
