<template>
  <div>
    <h1>당신을 위한 맞춤 문화재!</h1>
    <div class="d-flex">
      <HomeCardItem />
      <HomeCardItem />
      <HomeCardItem />
    </div>
  </div>
</template>

<script>
import HomeCardItem from "./HomeCardItem";

export default {
  name: "HomeHeritage",
  components: {
    HomeCardItem,
  },
};
</script>

<style></style>
