<template>
  <div>
    <h2>문화재 리뷰 작성 목록</h2>
    <div v-if="isEmpty">
      아직 등록된 리뷰가 없습니다.
      <!-- <button @click="goCreateReview">리뷰 작성하러가기</button> -->
    </div>
    <div v-else>
      <ul v-for="(result, i) in resultList" :key="i">
        <div @click="selectReview(result)">
          {{ result.title }}
          {{ result.created }}
        </div>
      </ul>
    </div>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";

export default {
  name: "MypageReview",
  created() {
    axios
      .get(SERVER.URL + SERVER.ROUTES.mypage + sessionStorage.nickname + "/")
      .then((res) => {
        this.reviewData = res.data.user.user_review;
        if (this.reviewData.length) {
          this.isEmpty = false;
        } else {
          this.isEmpty = true;
        }
      })
      .catch((err) => console.log(err));
  },
  methods: {
    selectReview(result) {
      this.$router.push({ name: "CommunityReviewItem", params: { result } });
    },
  },
  data() {
    return {
      reviewData: "",
      isEmpty: true,
    };
  },
};
</script>

<style></style>
