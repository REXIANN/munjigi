<template>
  <div class="community-review-item">
    <v-row>
      <v-btn dark @click="$router.push({ name: 'Community' })">목록보기</v-btn>
    </v-row>
    <div v-if="review.user == userData.nickname">
      <v-row justify="end">
        <v-dialog v-model="dialog" persistent max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn class="teal" dark v-bind="attrs" v-on="on" @click="connectReview()">수정</v-btn>
            <v-btn @click="deleteReview(review.id)">삭제</v-btn>
          </template>
          <v-card>
            <v-card-title>
              <h1>리뷰 수정하기</h1>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-text-field label="제목" v-model="title" required="제목을 입력해 주세요!" autofocus></v-text-field>
                <v-textarea
                  label="내용"
                  v-model="content"
                  required="내용을 입력해 주세요!"
                  @keypress.enter="updateReview(review.id)"
                ></v-textarea>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="error" text @click="dialog = false">
                <h3>닫기</h3>
              </v-btn>
              <v-btn color=" darken-1" text @click="updateReview(review.id)">
                <h3>작성완료</h3>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>
    </div>
    <h1>{{ reviewData.title }}</h1>
    <br />
    <h2>작성자 : {{ reviewData.user }}</h2>
    <h5>{{ reviewData.created_at }}</h5>
    <br />
    <h3>{{ reviewData.content }}</h3>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
import { mapState, mapGetters } from "vuex";

export default {
  name: "CommunityReviewItem",
  created() {
    this.userData.id = sessionStorage.id === undefined ? "" : sessionStorage.id;
    this.userData.nickname =
      sessionStorage.nickname === undefined ? "" : sessionStorage.nickname;
    axios
      .get(SERVER.URL + SERVER.ROUTES.review + this.review.id)
      .then((res) => (this.reviewData = res.data));
  },
  computed: {
    ...mapGetters(["config"]),
    ...mapState({ review: "review" }),
  },
  methods: {
    updateReview(id) {
      const reviewUpdateData = {
        title: this.title,
        content: this.content,
        user: this.userData.id,
      };
      axios
        .put(
          SERVER.URL + SERVER.ROUTES.review + id + "/",
          reviewUpdateData,
          this.config
        )
        .then(() => {
          this.dialog = false;
          axios
            .get(SERVER.URL + SERVER.ROUTES.review + this.review.id)
            .then((res) => (this.reviewData = res.data));
        })
        .catch((err) => {
          console.log(err.message);
        });
    },
    deleteReview(id) {
      axios
        .delete(SERVER.URL + SERVER.ROUTES.review + id)
        .then(() => {
          this.$router.push({ name: "Community" });
        })
        .catch((err) => {
          console.log(err.message);
        });
    },
    connectReview() {
      this.title = this.reviewData.title;
      this.content = this.reviewData.content;
    },
  },
  data() {
    return {
      userData: {
        id: "",
        nickname: "",
      },
      reviewData: {
        content: "",
        created_at: "",
        id: "",
        title: "",
        updated_at: "",
      },
      title: "",
      content: "",
      dialog: false,
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/community/communityReviewItem.scss";
</style>
