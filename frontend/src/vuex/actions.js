import axios from "axios";
// import cookies from 'vue-cookies'

// import router from '@/routes'
import SERVER from '@/api/drf'

export default {
  login({ state }, loginData) {
    // SET_TOKEN 해줘야 함
    axios.post(SERVER.URL + SERVER.ROUTES.login, loginData)
      .then((res) => {
        console.log(res)
        console.log(state)
        // sessionStorage.setItem("loginUID", res.data.object)
      })
      .catch((err) => console.log(err.message))

    // if(loginData.autoLogin) {
    // localStorage.setItem("loginUID", res.data.object)
    // } else {
    //   sessionStorage.setItem("loginUID", res.data.object)
    // }
    // commit("loginSuccess")
    // router.push({ name: "MyStudy", params: { UID: res.data.object } })
  },
  logout({ state }) {
    axios.post(SERVER)
      .then((res) => {
        console.log(res)
        state.auth_token = null
        localStorage.removeItem('loginUID')
        sessionStorage.removeItem('loginUID')
      })
      .catch((err) => { console.log(err.message) })


  },
  signup({ state }, signupData) {
    // 나중에 dispatch로 로그인도 해야 함
    axios.post(SERVER.URL + SERVER.ROUTES.signup, signupData)
      .then((res) => {
        console.log(res)
        console.log(state)
      })
      .catch((err) => console.log(err.message))
  },

};
