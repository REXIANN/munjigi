<template>
  <div class="mypageProfile">
    <h1>{{ userData.nickname }}님의 마이페이지</h1>
    <v-row justify="space-between">
      <v-col>
        <v-img
          src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg"
          alt="사용자 프로필 이미지"
          height="100px"
          width="100px"
        />
        <div>
          <button>프로필 사진 설정</button>
        </div>
      </v-col>
      <v-col>
        <h3>이름 : {{ userData.username }}</h3>
        <h3>성씨 본관 :{{ userData.ancestor }}</h3>
        <div>
          <v-btn @click="searchAncestor(userData.ancestor)">조상과 관련된 문화재 보기</v-btn>
        </div>
      </v-col>
      <v-col>
        <h3>현재 신분 {{ userData.grade }}</h3>
        <!-- <v-img
          class="grade-image"
          src="https://user-images.githubusercontent.com/60081201/93740775-20f36400-fc26-11ea-96ed-417389ec29eb.png"
          alt="양반등급 이미지"
          height="100px"
          width="100px"
        />-->
        <v-dialog v-model="gradeInfo" width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn class="ma-2" tile outlined color="success" v-bind="attrs" v-on="on">신분제알아보기</v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">문지기의 신분제</span>
              리뷰수로 신분이 결정됩니다.
            </v-card-title>
            <v-card-text>
              왕 : 리뷰 50개 이상 / 영의정 : 리뷰 30개 이상 / 기미상궁 : 리뷰
              20개 이상 / 사또 : 리뷰 10개 이상 / 양반 : 리뷰 5개 이상 / 천민 :
              리뷰 0개 이상
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="green darken-1" text @click="gradeInfo = false">닫기</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "MypageProfile",
  computed: {
    ...mapState(["userData"]),
  },
  data() {
    return {
      gradeInfo: false,
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/mypage/mypageProfile.scss";
</style>
