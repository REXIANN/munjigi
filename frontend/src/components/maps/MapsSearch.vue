<template>
  <div class="maps-search">
    This is MapsSearch.vue
    <br>
    <input type="text" v-model="keyword">
    <input type="submit" value="검색" >
  </div>
</template>

<script>
export default {
  name: "MapsSearch",
  data() {
    return {
      keyword: null,
    }
  }
}
</script>

<style>

</style>