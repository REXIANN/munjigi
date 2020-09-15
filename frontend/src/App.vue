<template>
  <v-app>
    <div id="nav">
      <v-row>
        <v-col cols="3">
          <router-link :to="{ name: 'Home' }">
            <img src="@/assets/logo.png" />
          </router-link>
        </v-col>
        <v-col>
          <router-link class="header" :to="{ name: 'Heritage' }">문화재</router-link>
          <router-link class="header" :to="{ name: 'Community' }">게시판</router-link>
          <router-link class="header" :to="{ name: 'Maps' }">지도</router-link>
          <router-link class="header_user" :to="{ name: 'Login' }">로그인</router-link>
          <router-link class="header_user" :to="{ name: 'Mypage' }">마이페이지</router-link>
        </v-col>
      </v-row>
    </div>
    <router-view />
  </v-app>
</template>

<style type="text/css" lang="scss">
  @import '@/assets/css/app.scss';
</style>
