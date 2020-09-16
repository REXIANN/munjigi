<template>
  <div>
    <div v-for="(review, idx) in reviewList" :key="idx">
      <v-card class="review-list" outlined @click="SELECT_REVIEW(review)">
        <v-list-item class="d-flex justify-space-around review-list-item">
          <v-img class="review-list-image" src="https://picsum.photos/510/300?random"></v-img>

          <div class="review-list-text">
            <div class="overline mb-4">{{ review.title }}</div>
            <v-list-item-subtitle>{{ review.user }}</v-list-item-subtitle>
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
      .get(SERVER.URL + SERVER.ROUTES.review + "/", null, null)
      .then((response) => {
        this.reviewList = response.data;
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

<style>
</style>