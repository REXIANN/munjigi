<template>
  <div class="home">
    This is Home.vue
    <p>{{ this.$store.state.count }}</p>
    <button @click="ADD_COUNT">change</button>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapMutations } from "vuex";

export default {
  name: "Home",
  methods: {
    ...mapMutations(['ADD_COUNT'])
  },
  data() {
    return {};
  },
};
</script>
