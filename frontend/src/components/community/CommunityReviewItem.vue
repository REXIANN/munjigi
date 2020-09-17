<template>
  <div>
    <div>
      <div v-if="review.user == userData.id">
        <v-row justify="end">
          <v-dialog v-model="dialog" persistent max-width="600px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn dark @click="deleteReview(review.id)">삭제</v-btn>
              <v-btn dark v-bind="attrs" v-on="on" @click="connectReview()">수정</v-btn>
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
import SERVER from "@/api/drf";
import axios from "axios";
import { mapState, mapGetters } from "vuex";

export default {
  name: "CommunityReviewItem",
  computed: {
    ...mapState(["userData"]),
    ...mapGetters(["config"]),
    ...mapState({ review: "review" }),
  },
  methods: {
    updateReview(id) {
      const reviewData = {
        title: this.title,
        content: this.content,
        user: this.userData.id,
      };
      axios
        .put(
          SERVER.URL + SERVER.ROUTES.review + "/" + id + "/",
          reviewData,
          this.config
        )
        .then(() => {
          this.dialog = false;
        })
        .catch((err) => {
          console.log(err.message);
        });
    },
    deleteReview(id) {
      axios
        .delete(SERVER.URL + SERVER.ROUTES.review + "/" + id)
        .then(() => {
          this.$router.push({ name: "Community" });
        })
        .catch((err) => {
          console.log(err.message);
        });
    },
    connectReview() {
      this.title = this.review.title;
      this.content = this.review.content;
    },
  },
  data() {
    return {
      title: "",
      content: "",
      dialog: false,
    };
  },
};
</script>

<style></style>
