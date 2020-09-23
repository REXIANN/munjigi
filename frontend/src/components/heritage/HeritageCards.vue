<template>
  <div class="heritageCards">
    <h1>인기 문화재</h1>
    <div class="row">
      <ul v-for="heritage in heritageList" :key="heritage.id">
        <v-hover v-slot:default="{ hover }">
          <v-card class="d-inline-block mx-auto">
            <v-container>
              <h3 @click="SELECT_HERITAGE(heritage)">{{ heritage.k_name }}</h3>
              <v-row justify="space-between">
                <v-col cols="auto">
                  <v-img height="200" width="200" :src="heritage.imageurl">
                    <v-expand-transition>
                      <div
                        v-if="hover"
                        class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal display-1 white--text"
                        style="height: 100%;"
                        @click="SELECT_HERITAGE(heritage)"
                      >{{ heritage.era }}</div>
                    </v-expand-transition>
                  </v-img>
                </v-col>
                <v-col cols="auto" class="text-center pl-0">
                  <v-row class="flex-column ma-0 fill-height" justify="center">
                    <v-col class="px-0">
                      <v-btn icon @click="like(heritage.id)">
                        <span v-if="heritage.like_users.includes(userDataId)">
                          <v-icon color="red lighten-2">mdi-heart</v-icon>
                        </span>
                        <span v-else>
                          <v-icon>mdi-heart</v-icon>
                        </span>
                      </v-btn>
                    </v-col>
                    <v-col class="px-0">
                      <v-btn icon @click="dib(heritage.id)">
                        <span v-if="heritage.dib_users.includes(userDataId)">
                          <v-icon color="green lighten-2">mdi-bookmark</v-icon>
                        </span>
                        <span v-else>
                          <v-icon>mdi-bookmark</v-icon>
                        </span>
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
      >목록의 끝입니다.</div>
    </infinite-loading>
  </div>
</template>

<script>
import InfiniteLoading from "vue-infinite-loading";
import SERVER from "@/api/drf";
import axios from "axios";
import { mapMutations, mapGetters } from "vuex";

export default {
  name: "CommunityCards",
  components: {
    InfiniteLoading,
  },
  mounted() {
    axios
      .get(SERVER.URL + SERVER.ROUTES.heritage + "/?page" + "=1")
      .then((res) => {
        this.heritageList = res.data.results;
      });
    this.userDataId = sessionStorage.id === undefined ? "" : sessionStorage.id;
  },
  computed: {
    ...mapGetters(["config"]),
  },
  methods: {
    ...mapMutations(["SELECT_HERITAGE"]),
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
    like(id) {
      axios
        .post(
          SERVER.URL + SERVER.ROUTES.heritage + id + "/like/",
          {
            userDataId: this.userDataId,
          },
          null
        )
        .then(() => {})
        .catch((err) => {
          console.error(err);
        });
    },
    dib(id) {
      axios
        .post(
          SERVER.URL + SERVER.ROUTES.heritage + id + "/dib/",
          {
            userDataId: this.userDataId,
          },
          null
        )
        .then(() => {})
        .catch((err) => {
          console.error(err);
        });
    },
  },
  data() {
    return {
      heritageList: [],
      limit: 2,
      userDataId: "",
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/heritage/heritageCards.scss";
</style>
