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
              >작성자 : {{ review.users }}</v-list-item-subtitle
            >
            <v-list-item-subtitle>{{ review.created_at }}</v-list-item-subtitle>
          </div>
        </v-list-item>
      </v-card>
    </div>
    <div v-if="reviewList.length >= 10">
      <infinite-loading @infinite="infiniteHandler" spinner="waveDots">
        <div
          slot="no-more"
          style="color: rgb(102, 102, 102); font-size: 14px; padding: 10px 0px"
        >
          목록의 끝입니다.
        </div>
      </infinite-loading>
    </div>
  </div>
</template>

<script>
import InfiniteLoading from "vue-infinite-loading";
import SERVER from "@/api/drf";
import axios from "axios";
import { mapMutations } from "vuex";

export default {
  name: "CommunityReviewList",
  components: {
    InfiniteLoading,
  },
  created() {
    axios
      .get(SERVER.URL + SERVER.ROUTES.review + "?page=1", null, null)
      .then((response) => {
        this.reviewList = response.data.results;
      });
  },
  methods: {
    ...mapMutations(["SELECT_REVIEW"]),
    infiniteHandler($state) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.review + "?page=" + this.limit)
        .then((response) => {
          setTimeout(() => {
            if (response.data.results) {
              this.reviewList = this.reviewList.concat(response.data.results);
              $state.loaded();
              this.limit += 1;
              const EACH_LEN = 10;
              if (response.data.results.length / EACH_LEN < 1) {
                $state.complete();
              }
            } else {
              // 끝 지정(No more data)
              $state.complete();
            }
          }, 1000);
        })
        .catch((err) => {
          console.error(err);
        });
      // } else {
      //   $state.complete();
      // }
    },
  },
  data() {
    return {
      reviewList: [],
      limit: 2,
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/community/communityReviewList.scss";
</style>
