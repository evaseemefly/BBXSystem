<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">首页</router-link> |
      <router-link to="/about">船舶状态</router-link>|
      <router-link to="/map">船舶显示</router-link>
      <router-link to="/state">状态显示</router-link>
    </div> -->
    <topMenu></topMenu>
    <router-view />
  </div>
</template>
<script>
import topMenu from './views/head/top_main_menu.vue';
export default {
  components: {
    topMenu
  }
}
</script>


<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
