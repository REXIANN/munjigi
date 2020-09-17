<template>
  <div>
    <h1>인기 문화재</h1>
    <button @click="check">체크</button>

    <h1 class="d-flex">
      <HeritageCardItem />
      <HeritageCardItem />
      <HeritageCardItem />
    </h1>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
import HeritageCardItem from "@/components/heritage/HeritageCardItem";

export default {
  name: "CommunityCards",
  components: {
    HeritageCardItem,
  },
  methods: {
    check() {
      axios
        .get(SERVER.URL + SERVER.ROUTES.heritage + "/?page" + "=1")
        .then((res) => {
          console.log(res);
        });
    },
  },
};
</script>

<style>
</style>