<template>
  <div>
    <h1>회원가입</h1>이름 :
    <input type="text" v-model="signupData.username" />
    닉네임 :
    <input type="text" v-model="signupData.nickname" />
    아이디 :
    <input type="email" v-model="signupData.email" />
    비밀번호 :
    <input type="password" v-model="signupData.password" />
    <div>
      <button @click="signup(signupData)">작성 완료</button>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Signup",
  methods: {
    ...mapActions(["signup"]),
  },
  data() {
    return {
      signupData: {
        username: "",
        nickname: "",
        email: "",
        password: "",
      },
    };
  },
};
</script>

<style>
</style>