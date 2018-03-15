import Vue from 'vue'
import generate from 'project-name-generator'
import eel from '../eel'
import router from '../../router'
import {onclose} from '../../socket'

const INCOMING = 1
const OUTGOING = 0

const uuidv4 = () => {
    return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>  // eslint-disable-line
        (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)  // eslint-disable-line
    )
}

const state = {
    available: [],
    currentSessions: {},
    sessionLogs: {}
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
        router.push({
            name: 'Workspace',
            params: {
                workspace: workspace.id
            }
        })
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
    UPDATE_SESSION_URL (state, {session, location}) {
        Vue.set(state.currentSessions[session.slug], 'location', location)
        eel.update_session(session.slug, session.id, 'location', location)
    },
    SET_SESSION (state, session) {
        Vue.set(state.currentSessions, session.slug, session)
        this.dispatch('fetchMessages', session)
    },
    NEW_SOCKET (state, workspace) {
        const currentSession = state.currentSessions[workspace.id]
        workspace.socket = new WebSocket(currentSession.location)
        workspace.socket.onmessage = (event) => {
            this.dispatch('logMessage', {session: currentSession, event})
        }
        workspace.socket.onclose = onclose
    },
    LOG_MESSAGE (state, {session, msg, message, direction}) {
        direction = (direction === INCOMING) ? 'INCOMING' : 'OUTGOING'
        if (!msg) {
            msg = {
                direction,
                message,
                id: uuidv4(),
                created: new Date()
            }

            eel.log_message(session.slug, session.id, msg)
        }
        const sessionId = `${session.slug}.${session.id}`
        if (!state.sessionLogs[sessionId]) {
            Vue.set(state.sessionLogs, sessionId, [])
        }
        state.sessionLogs[sessionId].push(msg)
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
    fetchMessages ({ commit }, session) {
        const run = eel.get_messages(session.slug, session.id)
        run(messages => {
            console.log(messages)
            messages.map(x => {
                commit('LOG_MESSAGE', {
                    session,
                    msg: x
                })
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
    sendMessage ({ commit, state }, {session, message}) {
        const workspace = this.getters.currentWorkspace
        workspace.socket.send(message)
        commit('LOG_MESSAGE', {session, message, direction: OUTGOING})
    },
    logMessage ({ commit }, {event, session}) {
        commit('LOG_MESSAGE', {session, message: event.data, direction: INCOMING})
    }
}

const getters = {
    currentWorkspace: (state, getters, rootState) => {
        const workspace = state.available.find(
            x => x.id === rootState.route.params.workspace)
        return workspace
    },
    currentSession: (state, getters) => {
        const workspace = getters.currentWorkspace
        if (workspace) {
            return state.currentSessions[workspace.id]
        } else {
            return null
        }
    },
    currentSessionLog: (state, getters) => {
        const session = getters.currentSession
        if (session) {
            const sessionId = `${session.slug}.${session.id}`
            return state.sessionLogs[sessionId] || []
        } else {
            return []
        }
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
