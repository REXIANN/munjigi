<template>
  <div>
    <MapsSearch />
    <div class="row maps-info-kakao">
      <MapsInfoList class="col-4" />
      <MapsKakao class="col-8" />
    </div>
  </div>
</template>

<script>
import MapsSearch from "@/components/maps/MapsSearch";
import MapsInfoList from "@/components/maps/MapsInfoList";
import MapsKakao from "@/components/maps/MapsKakao";

export default {
  name: "Maps",
  components: {
    MapsSearch,
    MapsInfoList,
    MapsKakao,
  },
  data() {
    return {};
  },
};
</script>

<style lang="scss">
@import "@/assets/css/views/maps.scss";
</style>