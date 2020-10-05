<template>
  <div class="community">
    <CommunityCreateReview />
    <CommunitySearchBar />
    <CommunityReviewList />
  </div>
</template>

<script>
import CommunitySearchBar from "@/components/community/CommunitySearchBar";
import CommunityCreateReview from "@/components/community/CommunityCreateReview";
import CommunityReviewList from "@/components/community/CommunityReviewList";

export default {
  name: "Community",
  components: {
    CommunitySearchBar,
    CommunityReviewList,
    CommunityCreateReview,
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/views/community.scss";
</style>