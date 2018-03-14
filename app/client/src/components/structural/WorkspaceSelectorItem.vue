<template>
    <div
        class="workspace-selector-item navbar-item"
        v-bind:class="{ active: isCurrent }">
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
        <span
            class="closer breathe-t-5 icon dark"
            v-on:click="closeWorkspace(workspace.id)">
            <close-icon />
        </span>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import CircleIcon from 'mdi-vue/CircleIcon'
import CloseIcon from 'mdi-vue/CloseIcon'
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
        isCurrent () {
            // console.log('this.info.id', this.info.id)
            // console.log('this.workspace.id', this.workspace.id)
            // console.log('this.currentWorkspace.id', this.currentWorkspace.id)
            // if (!this.currentWorkspace) {
            //     return false
            // }
            return this.currentWorkspace && this.workspace.id === this.currentWorkspace.id
        },
        workspace () {
            return this.activeWorkspaceById(this.info.id)
        },
        status () {
            return this.workspace.status || 0
        },
        ...mapGetters([
            'activeWorkspaceById',
            'currentWorkspace'
        ])
    },
    components: {
        CircleIcon,
        CircleOutlineIcon,
        AlertCircleOutlineIcon,
        CloseIcon
    },
    methods: {
        ...mapActions([
            'closeWorkspace'
        ])
    }
}
</script>

<style>
    .closer {
        display: block;
        line-height: 1;
        cursor: pointer;
    }
</style>
