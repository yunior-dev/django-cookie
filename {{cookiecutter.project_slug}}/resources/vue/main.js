/**
 * Here, we will create a fresh Vue application instance and attach it to
 * the page. Then, you may begin adding components to this application
 * or customize the JavaScript scaffolding to fit your unique needs.
 */
import Vue from 'vue'

import App from './layouts/App.vue'
import router from './router'


const app = new Vue({
  el: '#app',
  components: {
    App,
  },
  router,
})

export default app
