<template>
  <div>
    <h1>오늘의 인기 문화재!</h1>

    <!-- <VueSlickCarousel v-bind="settings">
      <div style="height:20vh;">1</div>
      <div style="height:20vh;">2</div>
      <div style="height:20vh;">3</div>
      <div style="height:20vh;">4</div>
      <div style="height:20vh;">5</div>
      <div style="height:20vh;">6</div>
      <div style="height:20vh;">7</div>
      <div style="height:20vh;">8</div>
      <div style="height:20vh;">9</div>
      <div style="height:20vh;">10</div>
    </VueSlickCarousel> -->
    <template>
      <v-carousel
        cycle
        height="300"
        hide-delimiter-background
        show-arrows-on-hover
      >
        <v-carousel-item v-for="(slide, i) in slides" :key="i">
          <v-sheet height="100%">
            <v-row no-gutters class="fill-height">
              <v-col class="fill-height">
                <v-card tile width="33%">
                  <!-- {{ heritageList[i].k_name }} -->
                  <img :src="heritageList[i].imageurl" />
                </v-card>
              </v-col>
              <v-col class="fill-height">
                <v-card tile width="34%">
                  <!-- {{ heritageList[i + 1].k_name }} -->
                  <img :src="heritageList[i + 1].imageurl" />
                </v-card>
              </v-col>
              <v-col class="fill-height">
                <v-card tile width="33%">
                  <!-- {{ heritageList[i + 2].k_name }} -->
                  <img :src="heritageList[i + 2].imageurl" />
                </v-card>
              </v-col>
            </v-row>
          </v-sheet>
        </v-carousel-item>
      </v-carousel>
    </template>
  </div>
</template>

<script>
// import "@/assets/css/components/heritage/heritageCarousel.scss";
// import VueSlickCarousel from "vue-slick-carousel";
// import "vue-slick-carousel/dist/vue-slick-carousel.css";
// import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
import SERVER from "@/api/drf";
import axios from "axios";

export default {
  name: "CommunityCarousel",
  // components: {
  //   VueSlickCarousel,
  // },
  mounted() {
    axios
      .get(SERVER.URL + SERVER.ROUTES.heritage + "?page" + "=1")
      .then((res) => {
        this.heritageList = res.data.results;
      });
  },
  data() {
    return {
      heritageList: [],

      slides: ["0", "1", "2", "3", "4", "5", "6", "7"],
      settings: {
        arrows: true,
        dots: true,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
        pauseOnDotsHover: true,
        pauseOnFocus: true,
        pauseOnHover: true,
      },
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/heritage/heritageCarousel.scss";
</style>
