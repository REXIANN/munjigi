<template>
  <div class="profile-update">
    <h1 class="profile-update-header">개인 정보 수정</h1>
    
    <div class="profile-update-block">
      <h3>이메일</h3>
      <span>이메일 주소는 변경하실 수 없습니다.</span>
      <input type="text" disabled v-model="userData.email" />
    </div>
    <div class="profile-update-block">
      <h3>이름</h3>
      <input type="text" v-model="userData.name" />
    </div>
    <div class="profile-update-block">
      <h3>닉네임</h3>
      <input type="text" v-model="userData.nickname" />
    </div>
    <div class="profile-update-block">
      <h3>생년월일</h3>
      <input type="text" v-model="userData.birth" />
    </div>

    <div class="submit-buttons">
      <input type="submit" value="나가기" @click="goPreviousPage" />
      <input type="submit" value="작성완료" @click="changeUserInfo" />
    </div>
  </div>
</template>

<script>
import axios from "axios"
import "@/assets/css/views/profileUpdate.scss";

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
  methods: {
    changeUserInfo() {
      const data = this.userData
      axios.put(`https://localhost:8080/accounts/${data.nickname}`, data)
        .then(res => {
          console.log(res)
          // 여기에 sessionStorage 업데이트 해주는 거 들어가야함
        })
        .catch(err => console.log(err))
    },
    goPreviousPage() {
      this.$router.go(-1)
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
    }
  },
};
</script>

<style>
</style>