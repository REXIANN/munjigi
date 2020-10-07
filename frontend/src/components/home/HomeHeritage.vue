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
import axios from "axios"
import SERVER from "@/api/drf"
import HomeCardItem from "./HomeCardItem";

export default {
  name: "HomeHeritage",
  components: {
    HomeCardItem,
  },
  created() {
    const URL = SERVER.URL + SERVER.ROUTES.recommend + sessionStorage.id
    console.log("URL", URL)
    axios.get(URL)
      .then(res => {
        console.log(res)
        this.recommendList = res.data
      })
      .catch(err => console.error(err))
  },
  data() {
    return {
      recommendList: []
    }
  }

};
</script>

<style></style>
