<template>
  <div class="profile-update">
    <h1 class="profile-update-header">개인 정보 수정</h1>
    
    <div class="profile-update-block">
      <h3>이메일</h3>
      <span>이메일 주소는 변경하실 수 없습니다.</span>
      <input type="text" disabled v-model="userData.email" />
    </div>
    <div class="profile-update-block">
      <h3>닉네임</h3>
      <span class="verify-nickname" @click="verifyNickname">닉네임 중복 확인하기</span>
      <input type="text" v-model="userData.nickname" />
    </div>
    <div class="profile-update-block">
      <h3>이름</h3>
      <input type="text" v-model="userData.name" />
    </div>
    <div class="profile-update-block">
      <h3>생년월일</h3>
      <input type="text" v-model="userData.birth" />
    </div>

    <div class="submit-buttons">
      <input type="submit" value="나가기" @click="goPreviousPage" />
      <input type="submit" value="작성완료" :disabled="!isNicknameVerified" @click="changeUserInfo" />
    </div>
  </div>
</template>

<script>
import axios from "axios"
import SERVER from "@/api/drf"
import "@/assets/css/views/profileUpdate.scss";
import { mapGetters } from "vuex"
export default {
  name: "ProfileUpdate",
  created() {
    if (sessionStorage.getItem("name") !== "undefined") {
      this.userData.name = sessionStorage.getItem("name")
    }
    if (sessionStorage.getItem("nickname") !== "undefined") {
      this.userData.nickname = sessionStorage.getItem("nickname")
    }
    if (sessionStorage.getItem("birth") !== "undefined") {
      this.userData.birth = sessionStorage.getItem("birth")
    }
  },
  computed: {
    ...mapGetters(["config"])
  },
  methods: {
    changeUserInfo() {
      const data = this.userData
      const URL = `${SERVER.URL}${SERVER.mypage}${data.nickname}/`
      axios.put(URL, data, this.config)
        .then(res => {
          console.log(res)
          // 여기에 sessionStorage 업데이트 해주는 거 들어가야함
        })
        .catch(err => console.log(err))
    },
    goPreviousPage() {
      this.$router.go(-1)
    },
    verifyNickname() {
      const URL = `${SERVER.URL}${SERVER.signup}${this.userData.nickname}/`
      console.log(URL)
      axios.get(URL)
        .then( res => {
          console.log(res)
          //닉네임이 사용가능하면 isNicknameVerified = true
        })
        .catch( err => console.log(err))
    }
  },
  data() {
    return {
      userData: {
        name: null,
        id: sessionStorage.getItem("id"),
        email: sessionStorage.getItem("email"),
        nickname: null,
        birth: null,
      },
      isNicknameVerified: false,
    }
  },
};
</script>

<style>
</style>