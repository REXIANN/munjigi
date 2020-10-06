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
    <div v-if="searchHeritageList.length">
      <v-row justify="center">
        <div>
          <v-expansion-panels popout>
            <v-expansion-panel
              v-for="(searchHeritage, idx) in searchHeritageList"
              :key="idx"
            >
              <v-expansion-panel-header>
                <h2>{{ searchHeritage.title }}</h2>
                {{ searchHeritage.users }}
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <h3>
                  {{ searchHeritage.content }}
                </h3>
                {{ searchHeritage.created_at }}
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </div>
      </v-row>
    </div>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";

export default {
  name: "CommunitySearchBar",
  created() {
    this.searchHeritageList = "";
  },
  methods: {
    searchInput() {
      if (this.searchSelectNum === 1) {
        console.log("1");
        const URL =
          SERVER.URL +
          SERVER.ROUTES.review +
          "search/title/?query=" +
          this.searchBar;
        axios.get(URL).then((res) => {
          this.searchHeritageList = res.data.results;
        });
      } else {
        console.log("2");
        axios
          .get(SERVER.URL + SERVER.ROUTES.mypage + this.searchBar + "/")
          .then((res) => {
            let userId = res.data.id;
            const URL =
              SERVER.URL +
              SERVER.ROUTES.review +
              "search/name/?query=" +
              userId;
            axios.get(URL).then((res) => {
              this.searchHeritageList = res.data.results;
            });
          });
      }
      this.searchBar = "";
    },
  },
  data() {
    return {
      searchBar: "",
      searchSelectNum: 1,
      searchType: ["제목", "작성자"],
      chooseType: "제목",
      searchHeritageList: [],
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/community/communitySearchBar.scss";
</style>