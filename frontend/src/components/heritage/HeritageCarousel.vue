<template> 
    <VueSlickCarousel v-bind="settings">
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
    </VueSlickCarousel>
</template>

<script>
import "@/assets/css/components/heritage/heritageCarousel.scss";
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";

export default {
  name: "CommunityCarousel",
  components: {
    VueSlickCarousel,
  },
  data() {
    return {
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

<style>
</style>