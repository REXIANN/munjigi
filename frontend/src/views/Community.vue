<template>
  <div>
      This is community.vue
      <CommunityReviewList />
  </div>
</template>

<script>
import CommunityReviewList from '@/components/community/CommunityReviewList'

export default {
  name: "Community",
  components: {
    CommunityReviewList,
  }
  
}
</script>

<style>

</style>