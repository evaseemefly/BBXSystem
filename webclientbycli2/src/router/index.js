import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import MyMap from '../views/content/center_map_base.vue'
import CenterState from '@/views/content/center_state'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/map',
      name: 'map',
      component: MyMap
    }, {
      path: '/area',
      name: 'area',
      component: CenterState
    }
  ]
})
