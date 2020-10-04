<template>
  <div class="signup">
    <form novalidate="true" class="box">
      <h1>회원가입</h1>
      <!-- 닉네임 -->
      <div>
        <h2>닉네임</h2>
        <!-- 닉네임 input tag -->
        <input
          type="text"
          v-model="signupData.nickname"
          placeholder="닉네임을 입력해주세요"
          @focusout="verifyNickname"
        />
        <h4 v-show="isNicknameVerified">사용가능</h4>
        <h4 v-show="!isNicknameVerified">사용불가능</h4>
      </div>

      <!-- 이메일 -->
      <div>
        <h2>이메일</h2>
        <button @click="verifyEmail">중복확인하기</button>
        <!-- 이메일 input tag -->
        <input
          type="text"
          placeholder="이메일을 입력해주세요"
          v-model="signupData.email"
          @focusout="verifyEmail"
        />
        <h4 v-show="!isEmailValidate">올바른 이메일 형식이 아닙니다</h4>
        <h4 v-show="isEmailVerified">사용가능한 이메일</h4>
        <h4 v-show="!isEmailVerified">사용불가능한 이메일</h4>
      </div>

      <!-- 비밀번호 -->
      <div>
        <h2>비밀번호</h2>
        <input type="password" v-model="signupData.password" />
      </div>

      <!-- 비밀번호 확인 -->
      <div>
        <h2>비밀번호 확인하기</h2>
        <input type="password" v-model="passwordConfirm" />
        <h4 v-show="isPasswordValidate">비밀번호가 일치합니다</h4>
        <h4 v-show="!isPasswordValidate">비밀번호가 일치하지 않습니다</h4>
      </div>

      <!-- 비밀번호 일치 여부 확인 -> active 넣어야 함 -->
      <div>
        <v-btn
          :disabled="!(isEmailVerified && isNicknameVerified && isEmailValidate && isPasswordValidate)"
          @click="signup(signupData)"
        >
          작성완료
        </v-btn>
      </div>
    </form>
  </div>
</template>

<script>
import "@/assets/css/views/signup.scss";
import SERVER from "@/api/drf";
import axios from "axios";
import { mapActions } from "vuex";

export default {
  name: "Signup",
  computed: {
    isEmailValidate() {
      const email = this.signupData.email;
      const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return pattern.test(email);
    },
    isPasswordValidate() {
      return this.signupData.password === this.passwordConfirm
    }
  },
  methods: {
    ...mapActions(["signup"]),
    verifyNickname() {
      const nickname = this.signupData.nickname;
      axios
        .get(SERVER.URL + SERVER.ROUTES.validity + nickname + "/")
        .then((res) => this.isNicknameVerified = res.data )
    },
    verifyEmail() {
      const email = this.signupData.email;
      axios
        .get(SERVER.URL + SERVER.ROUTES.validity + email + "/")
        .then((res) => this.isEmailVerified = res.data )
    },
  },
  data() {
    return {
      passwordConfirm: null,
      signupData: {
        nickname: "",
        email: "",
        password: "",
      },
      isNicknameVerified: false,
      isEmailVerified: false,
    };
  },
};
</script>

<style>
</style>