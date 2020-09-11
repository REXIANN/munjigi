<template>
  <div>
    This is CommunityReviewList.vue
    <div v-for="(result, idx) in resultList" :key="idx">
      
      <v-card class="mx-auto" max-width="400" outlined @click="selectReview(result)">
        <v-list-item>
          <v-list-item-content>
            <v-img :src="result.thumbnail" ></v-img>
            <div class="overline mb-4">{{ result.title }}</div>
            <v-list-item-subtitle>{{ result.user }}</v-list-item-subtitle>
            <v-list-item-subtitle>{{ result.view }}</v-list-item-subtitle>
            <v-list-item-subtitle>{{ result.created }}</v-list-item-subtitle>
          </v-list-item-content>

        </v-list-item>
      </v-card>
    </div>
  </div>
</template>

<script>

export default {
  name: "CommunityReviewList",
  methods: {
    selectReview(result) {
      this.$router.push({ name: "CommunityReviewItem", params: { result }})
    }
  },
  data() {
    return {
      resultList: [
        {
          thumbnail: "https://picsum.photos/510/300?random",
          title: "test1",
          user: "john",
          view: 1,
          created: "2020-09-23",
        },
        {
          thumbnail: "https://picsum.photos/510/300?random",
          title: "test2",
          user: "Harry",
          view: 22,
          created: "2020-09-23",
        },
        {
          thumbnail: "https://picsum.photos/510/300?random",
          title: "test3",
          user: "Taki",
          view: 33,
          created: "2020-09-23",
        },
        {
          thumbnail: "https://picsum.photos/510/300?random",
          title: "test4",
          user: "Cathy",
          view: 11,
          created: "2020-09-23",

        },
      ],
    };
  },
};
</script>

<style>
</style>