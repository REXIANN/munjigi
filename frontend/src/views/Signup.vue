<template>
  <div>
    <h1>회원가입</h1>

    <div>
      <div>
        <span>닉네임 : </span>
        <input type="text" v-model="signupData.nickname" />
        <button @click="checkNickname(signupData.nickname)">중복확인하기</button>
      </div>
      <div>
        <span>이메일 : </span>
        <input type="email" v-model="signupData.email" />
      <button @click="checkEmail(signupData.email)">중복확인하기</button>
      </div>
      <div>
        <span>비밀번호 : </span>
        <input type="password" v-model="signupData.password" />
      </div>
      <div>
        <span>비밀번호 확인하기 : </span>
        <input type="password" v-model="passwordConfirm" />
      </div>
    </div>

    <div>
      <!-- 비밀번호 일치 여부 확인해서 active 넣어야 함 -->
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
    checkEmail() {

    },
    checkNickname() {

    }
  },
  data() {
    return {
      passwordConfirm: null,
      signupData: {
        name: "",
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