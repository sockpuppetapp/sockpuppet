import Vue from 'vue'

import App from './App'
import router from './router'
import store from './store'
import { sync } from 'vuex-router-sync'

sync(store, router)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
    components: { App },
    router,
    store,
    template: '<App/>'
}).$mount('#app')
