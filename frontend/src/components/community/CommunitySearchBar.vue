<template>
  <div>
    <v-row class="search-input m-auto">
      <select
        class="search-input-select"
        v-model="searchSelectNum"
        label="제목"
      >
        <option selected value="1">제목</option>
        <option value="2">작성자</option>
      </select>

      <input
        class="search-input-width"
        type="text"
        v-model="searchBar"
        v-on:keyup.enter="searchInput()"
        append-icon="mdi-magnify"
        placeholder="검색어를 입력해주세요."
      />
    </v-row>
    {{ searchBar }}
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";

export default {
  name: "CommunitySearchBar",
  methods: {
    searchInput() {
      if (this.searchSelectNum === 1) {
        const URL =
          SERVER.URL +
          SERVER.ROUTES.review +
          "search/title/?query=" +
          this.searchBar;
        axios.get(URL).then((res) => {
          console.log(res);
          // this.searchHeritageList = res.data.results;
        });
      } else {
        axios
          .get(SERVER.URL + SERVER.ROUTES.mypage + this.searchBar + "/")
          .then((res) => {
            let userId = res.data.id;
            const URL =
              SERVER.URL +
              SERVER.ROUTES.review +
              "search/name/?query=" +
              userId;
            axios.get(URL).then((res) => console.log(res));
          });
      }
    },
  },
  data() {
    return {
      searchBar: "",
      searchSelectNum: 1,
      searchType: ["제목", "작성자"],
      chooseType: "제목",
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/community/communitySearchBar.scss";
</style>