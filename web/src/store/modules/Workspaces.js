import generate from 'project-name-generator'

const state = {
    inUse: []
}

const mutations = {
    OPEN_WORKSPACE (state, workspace) {
        state.inUse.push(workspace)
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
        commit('OPEN_WORKSPACE', workspace)
    }
}

const getters = {
    activeWorkspace: (state, getters, rootState) => {
        const workspace = state.inUse.find(
            x => x.id === rootState.route.params.workspace)
        return workspace
    }
}

export default {
    state,
    mutations,
    actions,
    getters
}
