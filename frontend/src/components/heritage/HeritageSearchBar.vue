<template>
  <div class="heritage-search-bar">
    <v-text-field class="" label="Main input" :rules="rules" hide-details="auto"></v-text-field>
  </div>
</template>

<script>
import "@/assets/css/components/heritage/heritageSearchBar.scss";

export default {
  name: "CommunitySearchBar",
  data() {
    return {
      rules: [
        (value) => !!value || "Required.",
        (value) => (value && value.length >= 3) || "Min 3 characters",
      ],
    };
  },
};
</script>
