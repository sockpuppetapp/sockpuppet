<template>
    <div class="workspace-selector-item navbar-item">
        <router-link :to="route" class="workspace-link">
            <span class="icon is-medium dark" v-if="status === 0">
                <circle-outline-icon />
            </span>
            <span class="icon is-medium danger" v-if="status === 1">
                <alert-circle-outline-icon />
            </span>
            <span class="icon is-medium warning" v-if="status === 2">
                <circle-outline-icon />
            </span>
            <span class="icon is-medium success" v-if="status === 3">
                <circle-icon />
            </span>
            {{info.name}}
        </router-link>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import CircleIcon from 'mdi-vue/CircleIcon'
import CircleOutlineIcon from 'mdi-vue/CircleOutlineIcon'
import AlertCircleOutlineIcon from 'mdi-vue/AlertCircleOutlineIcon'

// const statuses = [
//     {
//         class: '',
//         text: 'Connect'
//     },
//     {
//         class: 'was-error',
//         text: 'Connect'
//     },
//     {
//         class: 'in-progress',
//         text: 'Waiting'
//     },
//     {
//         class: 'is-connected',
//         text: 'Close'
//     }
// ]

export default {
    props: ['info'],
    data () {
        return {
            route: {
                name: 'Workspace',
                params: {
                    workspace: this.info.id
                }
            }
        }
    },
    computed: {
        workspace () {
            return this.activeWorkspaceById(this.info.id)
        },
        status () {
            return this.workspace.status || 0
        },
        ...mapGetters([
            'activeWorkspaceById'
        ])
    },
    components: {
        CircleIcon,
        CircleOutlineIcon,
        AlertCircleOutlineIcon
    }
}
</script>
