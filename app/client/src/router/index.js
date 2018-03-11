import Vue from 'vue'
import Router from 'vue-router'
import LandingPage from '../views/LandingPage'
import Workspace from '../views/Workspace'
import store from '../store'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/workspace/:workspace',
            name: 'Workspace',
            component: Workspace,
            beforeEnter: (to, from, next) => {
                const finder = store.state.Workspaces.available.find(
                    x => x.id === to.params.workspace)

                if (!finder) {
                    next({ name: 'Landing' })
                } else {
                    store.commit('SET_ACTIVE', finder)
                    next()
                }
            }
        },
        {
            path: '/',
            name: 'Landing',
            component: LandingPage
        }
    ]
})
