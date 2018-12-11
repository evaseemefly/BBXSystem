import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import jquery from 'jquery'
// import jQuery from 'jquery'
Vue.config.productionTip = false

window.jquery = window.$ = jquery
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
