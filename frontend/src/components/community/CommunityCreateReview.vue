<template>
  <div>
    <v-row justify="end">
      <v-dialog v-model="dialog" persistent max-width="600px">
        <template v-slot:activator="{ on, attrs }">
          <v-btn dark v-bind="attrs" v-on="on">새글쓰기</v-btn>
        </template>
        <v-card>
          <v-card-title>
            <h1>리뷰 작성하기</h1>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-text-field
                label="제목"
                v-model="title"
                hint="제목을 입력해주세요."
                required="제목을 입력해 주세요!"
                autofocus
              ></v-text-field>
              <v-textarea
                label="내용"
                v-model="content"
                hint="내용을 입력해주세요."
                required="내용을 입력해 주세요!"
                @keypress.enter="create"
              ></v-textarea>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="error" text @click="dialog = false">
              <h3>닫기</h3>
            </v-btn>
            <v-btn color=" darken-1" text @click="create">
              <h3>작성완료</h3>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
import { mapState, mapGetters } from "vuex";

export default {
  name: "CommunityCreateReview",
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
      this.dialog = false;
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

<style>
</style>