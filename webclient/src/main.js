import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import jquery from "jquery";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.js";
// import jQuery from 'jquery'
Vue.config.productionTip = false;
// 引入echarts
window.echarts = require("echarts");

window.jquery = window.$ = jquery;
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
