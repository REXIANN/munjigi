<template>
  <div class="home">
    <HomeIntroduce />
    <button @click="logout">logout</button>
    <HomeHeritage />
    <HomeCalendar />
  </div>
</template>

<script>
import HomeIntroduce from "@/components/home/HomeIntroduce.vue";
import HomeHeritage from "@/components/home/HomeHeritage.vue";
import HomeCalendar from "@/components/home/HomeCalendar.vue";
// import { mapMutations } from "vuex";
import { mapActions } from "vuex"

export default {
  name: "Home",
  components: {
    HomeIntroduce,
    HomeHeritage,
    HomeCalendar,
  },
  methods: {
    ...mapActions(['logout'])
  },
  data() {
    return {};
  },
};
</script>
