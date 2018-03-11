import Vue from 'vue'
import generate from 'project-name-generator'
import eel from '../eel'
import router from '../../router'

const state = {
    available: []
}

const mutations = {
    OPEN_WORKSPACE (state, workspace) {
        state.available.push(workspace)
    },
    SET_ACTIVE (state, workspace) {
        workspace.is_active = true
        eel.update_workspace(workspace.id, 'is_active', true)
    },
    REMOVE_ACTIVE (state, workspaceId) {
        state.available.find(
            x => x.id === workspaceId).is_active = false
        eel.update_workspace(workspaceId, 'is_active', false)
        router.push({ name: 'Landing' })
    },
    SET_STATUS (state, {workspace, status}) {
        const obj = state.available.find(
            x => x.id === workspace.id)
        Vue.set(obj, 'status', status)
    }
}

const actions = {
    newWorkspace ({ commit }) {
        const regex = /^([a-z]+)-([a-z]+)-[0-9]+$/g
        const subst = '$1 $2'
        const id = generate({number: true}).dashed
        const workspace = {
            id: id,
            name: id.replace(regex, subst)
        }
        eel.new_workspace(workspace.name)
        commit('OPEN_WORKSPACE', workspace)
    },
    fetchWorkspaces ({ commit }) {
        const info = eel.get_all_workspace_info()
        info(workspaces => {
            workspaces.map(x => {
                commit('OPEN_WORKSPACE', x)
            })
        })
    },
    closeWorkspace ({ commit }, workspaceId) {
        commit('REMOVE_ACTIVE', workspaceId)
    }
}

const getters = {
    currentWorkspace: (state, getters, rootState) => {
        const workspace = state.available.find(
            x => x.id === rootState.route.params.workspace)
        return workspace
    },
    activeWorkspaceById: (state) => (id) => {
        return state.available.find(x => x.id === id)
    }
}

export default {
    state,
    mutations,
    actions,
    getters
}
