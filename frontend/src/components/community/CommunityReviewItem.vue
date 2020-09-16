<template>
  <div>
    This is CommunityReviewItem.vue
    <div>
      <span>{{ review.title }}</span>
      <br />
      <span>{{ review.user }}</span>
      <br />
      <span>{{ review.content }}</span>
      <br />
      <span>{{ review.created_at }}</span>
      <br />
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "CommunityReviewItem",
  computed: {
    ...mapState({ review: "review" }),
  },
};
</script>

<style>
</style>