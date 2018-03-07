<template>
    <div class="workspace full">
        <div class="columns">
            <div id="sessions" class="column is-one-fifth">
                <div class="level">
                    <div class="level-left">
                        <div class="level-item">
                            <h2 class="is-size-4">{{activeWorkspace.name}}</h2>
                        </div>
                    </div>
                </div>
                <div class="level">
                    <div class="level-left">
                        <div class="level-item">
                            <h3>Sessions</h3>
                        </div>
                    </div>
                </div>
            </div>
            <div class="column is-four-fifths full">
                <vue-splitter :margin="20">
                    <div slot="left-pane" class="pane-wrap">
                        <location-input />
                        <message-input />
                    </div>
                    <div slot="right-pane">
                        <div class="level">
                            <div class="level-left">
                                <div class="level-item">
                                    <h2 class="is-size-4">Log</h2>
                                </div>
                            </div>
                        </div>
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

export default {
    computed: {
        id () {
            return this.$route.params.workspace
            // return this.$router.params.workspace
        },
        activeWorkspace () {
            return this.$store.getters.activeWorkspace
        }
    },
    components: {
        VueSplitter,
        LocationInput,
        MessageInput
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
