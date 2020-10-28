import Vue from 'vue'
import VueRouter from 'vue-router'
import NotFound from './errors/404.vue'

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
    },

    /**
     * ------------------------------------------------------------------------
     * This path uses a wildcard route that points to the 404.vue component.
     * ------------------------------------------------------------------------
    */
   {
    path: '*',
    name: '404 Not Found',
    component: NotFound,
    meta: { title: '404 Not Found' }
  }
  ]
})
