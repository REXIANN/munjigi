<template>
  <div class="home">
    This is Home.vue
    <p>{{ this.$store.state.test }}</p>
    <button @click="ADD">change</button>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapMutations } from 'vuex'
export default {
  name: 'Home',
  methods: {
    ...mapMutations(['ADD'])
  },
  data() {
    return {
    }
  }
}
</script>
