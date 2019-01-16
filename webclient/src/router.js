import Vue from "vue";
import Router from "vue-router";
// import Home from "./views/Home.vue";
import Map from "./views/home/index_map_bbx.vue";
import MyHome from "./views/home/index.vue";
// import Map from "./views/content/center_map_base.vue";
// import State from "./views/content/center_state.vue";
import State from "./views/home/index_state.vue";

import MainHome from "./App.vue";

import Search from "./views/home/index_search.vue";
import SearchWithTime from "@/views/home/index_search_with_time";
import iView from "iview";
import "../node_modules/iview/dist/styles/iview.css";
Vue.use(Router);
Vue.use(iView, {
  transfer: true,
  size: "large"
});

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    // {
    //   path: "",
    //   name: "default",
    //   component: Home
    // },
    {
      path: "",
      name: "default",
      meta: {
        title: "首页"
      },
      component: MainHome
    },
    {
      path: "/home",
      name: "home",
      meta: {
        title: "首页"
      },
      component: MyHome
    },
    {
      path: "/map/:kind",
      name: "map",
      meta: {
        title: "地图"
      },
      component: Map
    },
    {
      path: "/state",
      name: "state",
      meta: {
        title: "状态"
      },
      component: State
    },
    {
      path: "/search",
      name: "search",
      meta: {
        title: "查询"
      },
      component: Search
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/About.vue")
    },
    {
      path: "/searchWithTime",
      name: "searchWithTime",
      meta: {
        title: "查询"
      },
      component: SearchWithTime
    }
  ]
});
