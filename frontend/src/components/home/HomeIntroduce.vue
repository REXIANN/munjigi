<template>
  <div>
    <h1>소개</h1>
    <h2>문지기란?</h2>
    <h3 @click="goHeritage">문화재 추천</h3>사용자만을 위한 추천 서비스
    <h3 @click="goCommunity">게시판</h3>문화재 방문 리뷰 공유
    <h3 @click="goMap">지도</h3>문화재 위치와 주변 정보 제공
  </div>
</template>

<script>
export default {
  name: "HomeIntroduce",
  methods: {
    goHeritage() {
      this.$router.push({ name: "Heritage" });
    },
    goCommunity() {
      this.$router.push({ name: "Community" });
    },
    goMap() {
      this.$router.push({ name: "Maps" });
    },
  },
};
</script>

<style>
h3 {
  cursor: pointer;
}
</style>