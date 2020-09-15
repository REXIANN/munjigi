<template>
  <v-app id="app">
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

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  // text-align: center;
  color: #2c3e50;
}

#nav {
  background-image: url("https://user-images.githubusercontent.com/60081201/93159089-6d333580-f748-11ea-8ab2-7d14eb4737ec.png");
  background-size: contain;
  background-repeat: repeat;
  // text-align:
  img {
    height: 7vw;
    display: flex;
  }

  a {
    font-weight: bold;
    color: #4e2a2a;
    writing-mode: tb;
    text-decoration: none;
    &.header {
      background-image: url("https://user-images.githubusercontent.com/60081201/93159710-c780c600-f749-11ea-9ce3-426c9101f633.png");
    }
    &.header_user {
      background-image: url("https://user-images.githubusercontent.com/60081201/93162618-16c9f500-f750-11ea-9ddc-8c03d06098ae.png");
    }
    &.header.router-link-exact-active {
      color: white;
      background-image: url("https://user-images.githubusercontent.com/60081201/93162365-9c00da00-f74f-11ea-9b7c-e3e2298c002d.png");
    }
  }
}
</style>
