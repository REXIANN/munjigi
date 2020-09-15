<template>
  <v-app>
    <div id="nav">
      <router-link :to="{ name: 'Home' }">
        <img src="@/assets/logo.png" />
      </router-link>
      <router-link :to="{ name: 'Heritage' }">문화재</router-link>
      <router-link :to="{ name: 'Community' }">게시판</router-link>
      <router-link :to="{ name: 'Maps' }">지도</router-link>
      <router-link :to="{ name: 'Login' }">로그인</router-link>
      <router-link :to="{ name: 'Mypage' }">마이페이지</router-link>
    </div>
    <router-view />
  </v-app>
</template>

<style type="text/css" lang="scss">
  @import '@/assets/css/app.scss';
</style>
