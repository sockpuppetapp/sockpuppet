import Vue from 'vue'
import Vuex from 'vuex'
// import Store from 'electron-store'

import modules from './modules'

Vue.use(Vuex)

const vuex = new Vuex.Store({
    modules,
    strict: process.env.NODE_ENV !== 'production'
})

vuex.dispatch('fetchWorkspaces')

// vuex.persist = new Store({
//     name: 'sockpuppet'
// })

export default vuex
