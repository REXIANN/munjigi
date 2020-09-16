<template>
  <div class="heritage-search-bar">
    <v-text-field 
      name="input" 
      label="찾고자 하는 문화재를 검색해 보세요!" 
      :rules="rules" 
      hide-details="auto"></v-text-field>
  </div>
</template>

<script>
import "@/assets/css/components/heritage/heritageSearchBar.scss";

export default {
  name: "CommunitySearchBar",
  data() {
    return {
      rules: [
        (value) => !!value || "한 글자 이상 입력하셔야 합니다.",
      ],
    };
  },
};
</script>
