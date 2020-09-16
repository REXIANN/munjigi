<template>
  <div>
    <CommunityCreateReview />
    <CommunityReviewList />
  </div>
</template>

<script>
import CommunityReviewList from "@/components/community/CommunityReviewList";
import CommunityCreateReview from "@/components/community/CommunityCreateReview";

export default {
  name: "Community",
  components: {
    CommunityReviewList,
    CommunityCreateReview,
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/views/community.scss";
</style>