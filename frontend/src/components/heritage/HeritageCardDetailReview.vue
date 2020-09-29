<template>
  <div>
    <h3>리뷰 목록</h3>
    <div v-if="sessionStorage.id">리뷰 작성가능</div>
    <div v-for="review in heritageReviewList" :key="review.id">
      <v-row justify="center" no-gutters>
        <v-col lg="3">작성자 | {{ review.users }}</v-col>
        <v-col lg="3">
          <div class="pa-2" outlined tile>
            <h4>{{ review.title }}</h4>
            <h5>{{ review.content }}</h5>
            <small>{{ review.created_at }}</small>
          </div>
        </v-col>
      </v-row>
    </div>
    <div v-if="!heritageReviewList.length">
      <h5>관련 리뷰가 없습니다.</h5>
    </div>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";

export default {
  name: "HeritageCardDetailReview",
  created() {
    let heritageId = this.$route.params.id;
    axios
      .get(SERVER.URL + SERVER.ROUTES.heritage + heritageId)
      .then((res) => (this.heritageReviewList = res.data.heritage_reviews));
  },
  data() {
    return {
      heritageReviewList: "",
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/heritage/heritageCardDetailReview.scss";
</style>
