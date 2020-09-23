<template>
  <div class="mypage">
    <MypageProfile />
    <MypageMark />
    <MypageReview />
    <div class="mypage-buttons">
      <router-link :to="{ name: 'ProfileUpdate' }">정보 수정</router-link>
      <a href="#">회원탈퇴</a>
    </div>
  </div>
</template>

<script>
import MypageProfile from "@/components/mypage/MypageProfile.vue";
import MypageMark from "@/components/mypage/MypageMark.vue";
import MypageReview from "@/components/mypage/MypageReview.vue";
import "@/assets/css/views/mypage.scss";

export default {
  name: "Mypage",
  components: {
    MypageProfile,
    MypageMark,
    MypageReview,
  },
};
</script>

