<template>
  <v-app id="app">
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

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 10px;
  img {
    height: 7vw;
    display: flex;
  }

  a {
    font-weight: bold;
    color: #2c3e50;
    writing-mode: tb;
    text-decoration: none;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
