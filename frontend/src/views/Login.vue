<template>
  <div>
    <h1>로그인</h1>아이디 :
    <input type="text" v-model="loginData.username" placeholder="닉네임을 입력해주세요." autofocus />
    비밀번호 :
    <input type="password" v-model="loginData.password" />
    <div>
      <button @click="login(loginData)">로그인</button>
    </div>아직 회원이 아니신가요?
    <button @click="goSignup">회원가입하러 가기</button>
  </div>
</template>

<script>
// import { mapMutations } from "vuex";
import { mapActions } from "vuex";

export default {
  name: "Login",
  methods: {
    ...mapActions(["login"]),
    goSignup() {
      this.$router.push({ name: "Signup" });
    },
  },
  data() {
    return {
      loginData: {
        username: "",
        password: "",
      },
    };
  },
};
</script>

<style>
</style>