<template>
    <div class="workspace full">
        <div class="columns is-gapless">
            <workspace-sidebar workspace="currentWorkspace" />
            <div class="column is-four-fifths full">
                <vue-splitter :margin="20">
                    <div slot="left-pane" class="pane-wrap">
                        <location-input />
                        <message-input />
                    </div>
                    <div slot="right-pane" class="pane-wrap">
                        <message-log />
                    </div>
                </vue-splitter>
            </div>
        </div>
    </div>
</template>

<script>
import VueSplitter from '@rmp135/vue-splitter'
import LocationInput from '@/components/workspace/LocationInput'
import MessageInput from '@/components/workspace/MessageInput'
import MessageLog from '@/components/workspace/MessageLog'
import WorkspaceSidebar from '@/components/workspace/WorkspaceSidebar'

export default {
    components: {
        VueSplitter,
        LocationInput,
        MessageInput,
        WorkspaceSidebar,
        MessageLog
    },
    beforeRouteUpdate (to, from, next) {
        const finder = this.$store.state.Workspaces.available.find(
            x => x.id === to.params.workspace)

        if (!finder) {
            next({ name: 'Landing' })
        } else {
            this.$store.commit('SET_ACTIVE', finder)
            this.$store.commit('SET_SESSION', finder.sessions[0])
            next()
        }
    }
}
</script>

<style lang="scss">
    .workspace h2 { padding: 0.25rem 0 0 0.75rem; }
    .vue-splitter { height: 100%; }
    .column .level {
        height: 60px;
    }
    .pane-wrap {
        display: flex;
        flex-direction: column;
        flex: 1;
    }
    .splitter-pane {
        display: flex;
        flex-direction: column;
    }
</style>
