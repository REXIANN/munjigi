<template>
  <div class="community-review-list">
    <h1>문화재 방문 리뷰 게시판</h1>
    <div v-for="(review, idx) in reviewList" :key="idx">
      <v-card class="review-list" outlined @click="SELECT_REVIEW(review)">
        <v-list-item class="d-flex justify-space-around review-list-item">
          <v-img
            class="review-list-image"
            src="https://picsum.photos/510/300?random"
          ></v-img>

          <div class="review-list-text">
            <h3 class="mb-4">{{ review.title }}</h3>
            <v-list-item-subtitle
              >작성자 : {{ review.user }}</v-list-item-subtitle
            >
            <v-list-item-subtitle>{{ review.created_at }}</v-list-item-subtitle>
          </div>
        </v-list-item>
      </v-card>
    </div>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
import { mapMutations } from "vuex";

export default {
  name: "CommunityReviewList",
  mounted() {
    axios
      .get(SERVER.URL + SERVER.ROUTES.review + "/?page=1", null, null)
      .then((response) => {
        console.log(response.data);
        this.reviewList = response.data.results;
      });
  },
  methods: {
    ...mapMutations(["SELECT_REVIEW"]),
  },
  data() {
    return {
      reviewList: [],
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/community/communityReviewList.scss";
</style>
