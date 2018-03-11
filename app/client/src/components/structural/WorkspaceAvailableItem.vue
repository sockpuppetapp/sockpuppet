<template>
    <div class="workspace-available-item">
        <router-link
            :to="route"
            v-if="!workspace.is_active"
            class="workspace-link button is-primary is-outlined">
            {{workspace.name}}
        </router-link>
    </div>
</template>

<script>import { mapGetters } from 'vuex'
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
        ...mapGetters([
            'activeWorkspaceById'
        ])
    }
}
</script>
