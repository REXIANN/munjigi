<template>
  <div class="mypage">
    <MypageProfile />
    <MypageMark />
    <MypageReview />
    <div class="btn-end">
      <v-btn dark color="purple">개인 정보 수정</v-btn>
      <v-btn dark>탈퇴</v-btn>
    </div>
  </div>
</template>

<script>
import MypageProfile from "@/components/mypage/MypageProfile.vue";
import MypageMark from "@/components/mypage/MypageMark.vue";
import MypageReview from "@/components/mypage/MypageReview.vue";

export default {
  name: "Mypage",
  components: {
    MypageProfile,
    MypageMark,
    MypageReview,
  },
};
</script>

<style lang="scss">
@import "@/assets/css/views/mypage.scss";
</style>