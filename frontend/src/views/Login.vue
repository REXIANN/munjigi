<template>
  <div>
    <h1>로그인</h1>아이디 :
    <input type="text" v-model="nickname" placeholder="닉네임을 입력해주세요." autofocus />
    비밀번호 :
    <input type="password" v-model="password" />
    <div>
      <button @click="LOGIN">로그인</button>
    </div>아직 회원이 아니신가요?
    <button @click="goSignup">회원가입하러 가기</button>
  </div>
</template>

<script>
import { mapMutations } from "vuex";
// import router from "@/router";

export default {
  name: "Login",
  computed: {
    nickname: {
      get() {
        return this.$store.state.loginData.nickname;
      },
      // ...mapMutations(["UPDATE_NICKNAME"]),
      set(value) {
        this.$store.commit("UPDATE_NICKNAME", value);
      },
    },
    password: {
      get() {
        return this.$store.state.loginData.password;
      },
      set(value) {
        this.$store.commit("UPDATE_PASSWORD", value);
      },
    },
  },
  methods: {
    ...mapMutations(["LOGIN"]),
    // goSignup() {
    //   router.push({ name: "Signup" });
    // },
  },
};
</script>

<style>
</style>