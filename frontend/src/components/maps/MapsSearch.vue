<template>
  <div class="maps-search">
    <v-text-field 
      name="input" 
      label="지도에서 문화재를 찾아보세요!" 
      :rules="rules" 
      v-model="keyword"
      hide-details="auto"
      @keypress.enter="searchKeyword"  
    ></v-text-field>
      <input type="submit" value="검 색" @click="searchKeyword">
  </div>
</template>

<script>
import '@/assets/css/components/maps/mapsSearch.scss'

export default {
  name: "MapsSearch",
  methods: {
    searchKeyword() {
      console.log('search with', this.keyword) 
    }
  },
  data() {
    return {
      keyword: null,
      rules: [
        (value) => !!value || "한 글자 이상 입력하셔야 합니다.",
      ],
    }
  }
}
</script>

<style>

</style>