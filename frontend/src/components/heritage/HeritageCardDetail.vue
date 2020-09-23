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
      <div>
        <h2>{{ heritage.h_name }}</h2>
        <v-btn v-if="heritage.like_users.find((n) => n == userDataId)" icon color="red lighten-2">
          <v-icon @click="like(heritage.id)">mdi-heart</v-icon>
        </v-btn>
        <v-btn v-else icon>
          <v-icon @click="like(heritage.id)">mdi-heart</v-icon>
        </v-btn>

        <v-btn v-if="heritage.dib_users.find((n) => n == userDataId)" icon color="green lighten-2">
          <v-icon @click="dib(heritage.id)">mdi-bookmark</v-icon>
        </v-btn>
        <v-btn v-else icon>
          <v-icon @click="dib(heritage.id)">mdi-bookmark</v-icon>
        </v-btn>
      </div>
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

export default {
  name: "HeritageCardDetail",
  created() {
    this.userDataId = sessionStorage.id === undefined ? "" : sessionStorage.id;
    let heritageId = this.$route.params.id;
    axios
      .get(SERVER.URL + SERVER.ROUTES.heritage + heritageId)
      .then((res) => (this.heritage = res.data));
  },
  methods: {
    like(id) {
      axios
        .post(
          SERVER.URL + SERVER.ROUTES.heritage + id + "/like/",
          {
            userDataId: this.userDataId,
          },
          null
        )
        .then(() => {
          axios
            .get(SERVER.URL + SERVER.ROUTES.heritage + id)
            .then((res) => (this.heritage = res.data));
        })
        .catch((err) => {
          console.error(err);
        });
    },
    dib(id) {
      axios
        .post(
          SERVER.URL + SERVER.ROUTES.heritage + id + "/dib/",
          {
            userDataId: this.userDataId,
          },
          null
        )
        .then(() => {
          axios
            .get(SERVER.URL + SERVER.ROUTES.heritage + id)
            .then((res) => (this.heritage = res.data));
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  data() {
    return {
      userDataId: "",
      heritage: {},
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/heritage/heritageCardDetail.scss";
</style>
