<template>
  <div>
    <h1>회원가입</h1>

    <form novalidate="true">
      <div>
        <span>닉네임 : </span>
        <input type="text" v-model="signupData.nickname" />
        <button @click="checkNickname(signupData.nickname)">
          중복확인하기
        </button>
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
    </form>

    <div v-if="checkMail && checkNick">
      <!-- 비밀번호 일치 여부 확인해서 active 넣어야 함 -->
      <v-btn @click="signup(signupData)">작성 완료</v-btn>
    </div>
    <div v-else>
      <v-btn disabled> 작성완료 </v-btn>
    </div>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
import { mapActions } from "vuex";

export default {
  name: "Signup",
  methods: {
    ...mapActions(["signup"]),
    checkNickname(nickname) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.validity + nickname + "/")
        .then((res) => {
          if (res.data == true) {
            alert("사용가능한 닉네임입니다.");
            this.checkNick = true;
          } else {
            alert("새로운 닉네임을 입력해주세요.");
            this.signupData.nickname = "";
          }
        })
        .catch((err) => console.log(err));
    },

    checkEmail(email) {
      if (email.indexOf("@") === -1) {
        alert("이메일 양식을 지켜주세요!");
        this.$refs.signupData.email.focus();
        return;
      } else {
        axios
          .get(SERVER.URL + SERVER.ROUTES.validity + email + "/")
          .then((res) => {
            if (res.data == true) {
              alert("사용가능한 이메일입니다.");
              this.checkMail = true;
            } else {
              alert("존재하는 이메일입니다.");
              this.signupData.email = "";
            }
          })
          .catch((err) => console.log(err));
      }
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
      checkNick: false,
      checkMail: false,
    };
  },
};
</script>

<style lang="scss">
@import "@/assets/css/views/login.scss";
</style>