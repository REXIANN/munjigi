<template>
  <div class="heritageCardDetail">
    <v-container>
      <v-row no-gutters>
        <h1>{{ heritage.k_name }}</h1>
        <v-chip class="ma-5" color="orange" text-color="white">
          {{ heritage.clsfc_name }}
          <v-icon right>mdi-star</v-icon>
        </v-chip>
      </v-row>
      <h2>{{ heritage.h_name }}</h2>
      <button @click="like(heritage.id)">좋아요</button>
      <v-row>
        <v-col cols="4">
          <v-img :src="heritage.imageurl" :alt="heritage.k_name" width="300vw" />
        </v-col>
        <v-col cols="8">
          <h5>{{ heritage.content }}</h5>
        </v-col>
      </v-row>
    </v-container>
    <br />
    <h3>위치 정보</h3>
    <p>{{ heritage.address }}</p>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
import { mapState } from "vuex";

export default {
  name: "HeritageCardDetail",
  computed: {
    ...mapState({ heritage: "heritage" }),
  },
  methods: {
    like(id) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.heritage + "/" + id + "/like")
        .then((resp) => {
          console.log(resp);
        });
    },
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/heritage/heritageCardDetail.scss";
</style>
