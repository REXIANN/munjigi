<template>
  <div>
    <CommunityCreateReview />
    <CommunityReviewList />
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
// import { mapMutations } from "vuex";
import CommunityReviewList from "@/components/community/CommunityReviewList";
import CommunityCreateReview from "@/components/community/CommunityCreateReview";

export default {
  name: "Community",
  components: {
    CommunityReviewList,
    CommunityCreateReview,
  },
  created() {
    axios
      .get(SERVER.URL + SERVER.ROUTES.review + "/", null, null)
      .then((response) => {
        console.log(response);
      });
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/views/community.scss";
</style>