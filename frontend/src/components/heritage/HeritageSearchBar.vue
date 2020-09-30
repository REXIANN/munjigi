<template>
  <div class="heritage-search-bar">
    <v-text-field
      name="input"
      label="찾고자 하는 문화재를 검색해 보세요!"
      append-icon="mdi-magnify"
      :rules="rules"
      v-model="searchInput"
      hide-details="auto"
      @keypress="searchHeritage(searchInput)"
    ></v-text-field>
    {{ searchHeritageList }}
  </div>
</template>

<script>
import "@/assets/css/components/heritage/heritageSearchBar.scss";
import SERVER from "@/api/drf";
import axios from "axios";

export default {
  name: "CommunitySearchBar",
  methods: {
    searchHeritage(searchInput) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.heritage + "?query=" + searchInput)
        .then((res) => {
          console.log(res.data.results);
          this.searchHeritageList = res.data.results;
        });
    },
  },
  data() {
    return {
      searchInput: "",
      searchHeritageList: [],
      rules: [(value) => !!value || "한 글자 이상 입력하셔야 합니다."],
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/heritage/heritageSearchBar.scss";
</style>