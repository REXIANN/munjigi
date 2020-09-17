<template>
  <div class="heritageCards">
    <h1>인기 문화재</h1>
    <!-- {{ heritageList}} -->
    <div class="row">
      <ul v-for="heritage in heritageList" :key="heritage.id">
        <v-hover v-slot:default="{ hover }">
          <v-card class="d-inline-block mx-auto">
            <v-container>
              <h3>{{ heritage.k_name }}</h3>
              <v-row justify="space-between">
                <v-col cols="auto">
                  <v-img height="200" width="200" :src="heritage.imageurl">
                    <v-expand-transition>
                      <div
                        v-if="hover"
                        class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal display-1 white--text"
                        style="height: 100%;"
                      >{{ heritage.era }}</div>
                    </v-expand-transition>
                  </v-img>
                </v-col>
                <v-col cols="auto" class="text-center pl-0">
                  <v-row class="flex-column ma-0 fill-height" justify="center">
                    <v-col class="px-0">
                      <v-btn icon>
                        <v-icon>mdi-heart</v-icon>
                      </v-btn>
                    </v-col>
                    <v-col class="px-0">
                      <v-btn icon>
                        <v-icon>mdi-bookmark</v-icon>
                      </v-btn>
                    </v-col>
                    <v-col class="px-0">
                      <v-btn icon>
                        <v-icon>mdi-share-variant</v-icon>
                      </v-btn>
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-hover>
      </ul>
    </div>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
// import HeritageCardItem from "@/components/heritage/HeritageCardItem";

export default {
  name: "CommunityCards",
  components: {
    // HeritageCardItem,
  },
  mounted() {
    axios
      .get(SERVER.URL + SERVER.ROUTES.heritage + "/?page" + "=1")
      .then((res) => {
        this.heritageList = res.data.results;
      });
  },
  methods: {},
  data() {
    return {
      heritageList: [],
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/heritage/heritageCards.scss";
</style>
