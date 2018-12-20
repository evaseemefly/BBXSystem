import Vue from "vue";
import Router from "vue-router";
// import Home from "./views/Home.vue";
import Home from "./views/home/index_map_bbx.vue";
import MyHome from "./views/home/index.vue";
import Map from "./views/content/center_map_base.vue";
import State from "./views/content/center_state.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "",
      name: "default",
      component: Home
    },
    {
      path: "/home",
      name: "home",
      component: MyHome
    },
    {
      path: "/map",
      name: "map",
      component: Map
    },
    {
      path: "/state",
      name: "state",
      component: State
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/About.vue")
    }
  ]
});
