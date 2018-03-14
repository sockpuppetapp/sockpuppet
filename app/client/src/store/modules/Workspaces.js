import Vue from 'vue'
import generate from 'project-name-generator'
import eel from '../eel'
import router from '../../router'
import {onmessage, onclose} from '../../socket'

const state = {
    available: [],
    currentSession: null,
    socket: null
}

const mutations = {
    OPEN_WORKSPACE (state, workspace) {
        const index = state.available.findIndex(
            x => x.id === workspace.id)

        if (index >= 0) {
            state.available.splice(index, 1)
        }

        state.available.push(workspace)
        // TEMP
        // router.push({
        //     name: 'Workspace',
        //     params: {
        //         workspace: workspace.id
        //     }
        // })
    },
    SET_ACTIVE (state, workspace) {
        workspace.is_active = true
        eel.update_workspace(workspace.id, 'is_active', true)
    },
    UPDATE_WORKSPACE_NAME (state, {workspace, name}) {
        workspace.name = name
        eel.update_workspace(workspace.id, 'name', name)
    },
    REMOVE_ACTIVE (state, {workspaceId}) {
        const workspace = state.available.find(
            x => x.id === workspaceId)
        if (workspace) {
            workspace.is_active = false
            eel.update_workspace(workspaceId, 'is_active', false)
        }

        // TODO:
        // - Only push to landing if it was current
        router.push({ name: 'Landing' })
    },
    SET_STATUS (state, {workspace, status}) {
        const obj = state.available.find(
            x => x.id === workspace.id)
        Vue.set(obj, 'status', status)
    },
    NEW_SESSION (state, workspaceId) {
        eel.new_session(workspaceId)
        this.dispatch('fetchWorkspaces')
    },
    CLEAR_SESSION (state) {
        state.currentSession = null
    },
    UPDATE_SESSION_URL (state, url) {
        state.currentSession.location = url
        eel.update_session(state.currentSession.slug, state.currentSession.id, 'location', url)
    },
    SET_SESSION (state, session) {
        state.currentSession = session
    },
    NEW_SOCKET (state, workspace) {
        // TODO:
        // - When opening socket, attach to workspace object
        // workspace.socket = new WebSocket(session.location)
        // workspace.socket.onmessage = onmessage
        // workspace.socket.onclose = onclose
    }
}

const actions = {
    newWorkspace ({ commit }) {
        const regex = /^([a-z]+)-([a-z]+)-[0-9]+$/g
        const subst = '$1 $2'
        const id = generate({number: true}).dashed
        const name = id
            .replace(regex, subst)
            .split(' ')
            .map(x => x.charAt(0).toUpperCase() + x.slice(1))
            .join(' ')
        const workspace = {
            id: id,
            name: name
        }
        eel.new_workspace(workspace.name, workspace.id)
        commit('OPEN_WORKSPACE', workspace)
        commit('SET_ACTIVE', workspace)
        this.dispatch('fetchWorkspaces')
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
        commit('REMOVE_ACTIVE', {workspaceId})
    },
    newSession ({ commit }, workspaceId) {
        commit('NEW_SESSION', workspaceId)
    },
    setSession ({ commit }, session) {
        commit('SET_SESSION', session)
    },
    sendMessage ({ commit }, {session, msg}) {
        console.log('sending message', msg)
        session.socket.send(msg)
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
