<template>
  <div>
    <div>
      <input type="text" v-model="title" placeholder="제목을 입력해주세요" autofocus required="제목을 입력해 주세요!" />
      <input
        type="text"
        v-model="content"
        placeholder="내용을 입력해주세요"
        autofocus
        required="내용을 입력해 주세요!"
        @keypress.enter="create"
      />
      <input type="submit" value="작성완료" @click="create" />
    </div>
    <button @click="getReview">불러오기</button>
    <CommunityReviewList />
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
import CommunityReviewList from "@/components/community/CommunityReviewList";
import { mapState, mapGetters, mapActions } from "vuex";

export default {
  name: "Community",
  components: {
    CommunityReviewList,
  },
  created: {},
  computed: {
    ...mapState(["userData"]),
    ...mapGetters(["config"]),
  },
  methods: {
    create() {
      const reviewData = {
        title: this.title,
        content: this.content,
        user: this.userData.id,
      };
      axios.post(
        SERVER.URL + SERVER.ROUTES.review + "/",
        reviewData,
        this.config
      );
    },
    ...mapActions(["getReview"]),
  },
  data() {
    return {
      title: "",
      content: "",
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/views/community.scss";
</style>