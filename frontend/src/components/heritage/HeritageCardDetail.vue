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
        <v-btn v-if="isUserLike" icon color="red lighten-2">
          <v-icon @click="like(heritage.id)">mdi-heart</v-icon>
        </v-btn>
        <v-btn v-else icon>
          <v-icon @click="like(heritage.id)">mdi-heart</v-icon>
        </v-btn>

        <v-btn v-if="isUserDib" icon color="green lighten-2">
          <v-icon @click="dib(heritage.id)">mdi-bookmark</v-icon>
        </v-btn>
        <v-btn v-else icon>
          <v-icon @click="dib(heritage.id)">mdi-bookmark</v-icon>
        </v-btn>
      </div>
      <v-row>
        <v-col cols="4">
          <v-img
            :src="heritage.imageurl"
            :alt="heritage.k_name"
            width="300vw"
          />
        </v-col>
        <v-col cols="8">
          <h5>{{ heritage.content }}</h5>
        </v-col>
      </v-row>
    </v-container>
    <br />
    <!-- 문화재의 평점을 보여주는 블록 -->
    <div>
      <h2>이 문화재의 평점은 {{ this.ratingAvg}}점 입니다</h2>
    </div>

    <!-- 사용자가 평점을 매기는 블록 -->
    <div class="d-flex flex-column align-center my-4">
      <h2>평점을 매겨보세요!</h2>
      <div>
        <star-rating v-model="rating"></star-rating>
        <v-btn color="yellow" @click="setRating"> 평점 매기기! </v-btn>
      </div>
    </div>

    <!-- 위치정보  -->
    <h3>위치 정보</h3>
    <p>{{ heritage.address }}</p>
    <HeritageCardDetailReview />
  </div>
</template>

<script>
import StarRating from "vue-star-rating";
import SERVER from "@/api/drf";
import axios from "axios";
import { mapGetters } from "vuex";
import HeritageCardDetailReview from "@/components/heritage/HeritageCardDetailReview";

export default {
  name: "HeritageCardDetail",
  components: {
    HeritageCardDetailReview,
    StarRating,
  },
  created() {
    this.userDataId =
      sessionStorage.id === undefined ? null : sessionStorage.id;
    let heritageId = this.$route.params.id;
    axios
      .get(SERVER.URL + SERVER.ROUTES.heritage + heritageId)
      .then((res) => (this.heritage = res.data));
  },
  mounted() {
    // get rating of the heritage
    let heritageId = this.$route.params.id;
    const URL = SERVER.URL + SERVER.ROUTES.heritage + heritageId + "/score/";
    axios
      .get(URL)
      .then((res) => {
        this.ratingList = res.data;
      })
      .catch((err) => console.log(err));
  },
  computed: {
    ...mapGetters(["config"]),
    // heritageScore() {
    // const arr = this.ratingList
    // arr.forEach((elem) => console.log(elem) )
    ratingAvg() {
      const arr = this.ratingList
        let sum = 0;
        arr.forEach((elem) => (sum += elem.rating + 3));
        return sum / arr.length
    },
    // },
    isUserLike() {
      return (
        this.heritage.like_users &&
        this.heritage.like_users.includes(Number(this.userDataId))
      );
    },
    isUserDib() {
      return (
        this.heritage.dib_users &&
        this.heritage.dib_users.includes(Number(this.userDataId))
      );
    },
  },
  methods: {
    setRating() {
      const URL =
        SERVER.URL + SERVER.ROUTES.heritage + this.heritage.id + "/score/";
      const data = {
        heritage: this.heritage.id,
        rating: this.rating - 3,
        user: Number(this.userDataId),
      };
      axios
        .post(URL, data, this.config)
        .then((res) => (this.ratingList = res.data))
        .catch(() => alert("로그인 후 이용가능한 기능입니다."));
    },
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
      rating: 3,
      userDataId: null,
      heritage: {},
      ratingList: {
        type: Array,
      },
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/heritage/heritageCardDetail.scss";
</style>
