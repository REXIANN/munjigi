<template>
  <div>
    <h2>찜한 문화재 목록</h2>
    <div v-if="isEmpty">
      아직 등록된 문화재가 없습니다.
      <button @click="goHeritage">추천 문화재 보러가기</button>
    </div>
    <div v-else>
      <ul v-for="(dib, i) in dibData" :key="i">
        <h5 class="cursor" @click="goDib(dib)">{{ dib }}</h5>
      </ul>
    </div>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";

export default {
  name: "MypageDib",
  created() {
    axios
      .get(SERVER.URL + SERVER.ROUTES.mypage + sessionStorage.nickname + "/")
      .then((res) => {
        this.dibData = res.data.user.dibs_heritages;
        console.log(this.dibData.length);
        if (this.dibData.length) {
          this.isEmpty = false;
        } else {
          this.isEmpty = true;
        }
      })
      .catch((err) => console.log(err));
  },
  methods: {
    goHeritage() {
      this.$router.push({ name: "Heritage" });
    },
    goDib(dib) {
      this.$router.push({ name: "HeritageCardDetail", params: { id: dib } });
    },
  },
  data() {
    return {
      isEmpty: true,
      dibData: [],
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/mypage/mypageDib.scss";
</style>

