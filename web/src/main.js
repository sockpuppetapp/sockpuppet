import Vue from 'vue'

import App from './App'
import router from './router'
import store from './store'
import { sync } from 'vuex-router-sync'

// import SystemJS from 'systemjs'
// SystemJS.import('http://localhost:8888/eel.js').then(function (eel) {
//     console.log(eel)
// })

sync(store, router)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
    components: { App },
    router,
    store,
    template: '<App/>'
}).$mount('#app')
