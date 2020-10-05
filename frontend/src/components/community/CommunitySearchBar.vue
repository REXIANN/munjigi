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
export default {
  name: "CommunitySearchBar",
  methods: {
    searchInput() {
      if (this.searchSelectNum === 1) {
        console.log("제목 검색일 경우");
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