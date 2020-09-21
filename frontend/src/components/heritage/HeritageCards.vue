<template>
  <div class="heritageCards">
    <h1>이런 문화재, 알고 계셨나요?</h1>
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
                      >
                        {{ heritage.era }}
                      </div>
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

    <infinite-loading @infinite="infiniteHandler" spinner="waveDots">
      <div
        slot="no-more"
        style="color: rgb(102, 102, 102); font-size: 14px; padding: 10px 0px;"
      >
        목록의 끝입니다.
      </div>
    </infinite-loading>
  </div>
</template>

<script>
import InfiniteLoading from "vue-infinite-loading";
import SERVER from "@/api/drf";
import axios from "axios";
// import HeritageCardItem from "@/components/heritage/HeritageCardItem";

export default {
  name: "CommunityCards",
  components: {
    InfiniteLoading,
    // HeritageCardItem,
  },
  mounted() {
    axios
      .get(SERVER.URL + SERVER.ROUTES.heritage + "/?page" + "=1")
      .then((res) => {
        this.heritageList = res.data.results;
      });
  },
  methods: {
    infiniteHandler($state) {
      axios
        .get(SERVER.URL + SERVER.ROUTES.heritage + "/?page=" + this.limit)
        .then((response) => {
          setTimeout(() => {
            if (response.data.results) {
              this.heritageList = this.heritageList.concat(
                response.data.results
              );
              $state.loaded();
              this.limit += 1;
              const EACH_LEN = 10;
              if (response.data.results.length / EACH_LEN < 1) {
                $state.complete();
              }
            } else {
              // 끝 지정(No more data)
              $state.complete();
            }
          }, 1000);
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  data() {
    return {
      heritageList: [],
      limit: 2,
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/heritage/heritageCards.scss";
</style>
