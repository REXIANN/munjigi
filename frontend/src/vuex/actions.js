import axios from "axios";
import cookies from 'vue-cookies'

// import router from '@/routes'
import SERVER from '@/api/drf'

export default {
  login({ }, loginData) {
    axios.post(SERVER, loginData)
      .then((res) => {
        console.log(res)
        sessionStorage.setItem("loginUID", res.data.object)
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
  signup({ state, commit }, signupData) {
    axios.post(SERVER, signupData)
      .then((res) => console.log(res))
      .catch((err) => console.log(err.message))
  },

};
