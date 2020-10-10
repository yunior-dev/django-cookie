import Vue from 'vue'
import VueRouter from 'vue-router'

import Welcome from './pages/Welcome.vue'

Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'welcome',
      component: Welcome,
      meta: { title: 'Welcome' }
    }
  ]
})
