<template>
  <div class="mypage">
    <MypageProfile />
    <MypageDib />
    <MypageReview />
    <div class="btn-end">
      <v-btn dark color="purple">개인 정보 수정</v-btn>
      <v-btn dark>탈퇴</v-btn>
    </div>
  </div>
</template>

<script>
import MypageProfile from "@/components/mypage/MypageProfile.vue";
import MypageDib from "@/components/mypage/MypageDib.vue";
import MypageReview from "@/components/mypage/MypageReview.vue";
import "@/assets/css/views/mypage.scss";

export default {
  name: "Mypage",
  components: {
    MypageProfile,
    MypageDib,
    MypageReview,
  },
};
</script>

