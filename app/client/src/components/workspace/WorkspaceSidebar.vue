<template>
    <div id="sessions" class="column is-one-fifth">
        <section>
            <input
                type="text"
                v-bind:value="currentWorkspace.name"
                @input="updateWorkspaceName"
                class="is-size-4">
        </section>
        <section>
            <div class="sessions">
                <h3 class="is-size-5 breathe-10">Sessions</h3>
                <workspace-sessions />
                <a
                    v-on:click="newSession(id)"
                    class="button is-small is-primary breathe-10">Start new session</a>
            </div>
        </section>
        <section>
            <div class="sessions">
                <a
                    v-on:click="closeWorkspace(id)"
                    class="button is-small is-light is-outlined breathe-10">Close workspace</a>
                </div>
        </section>
    </div>
</template>

<script>
import { mapActions } from 'vuex'
import WorkspaceSessions from '@/components/workspace/WorkspaceSessions'

export default {
    computed: {
        id () {
            return this.$route.params.workspace
            // return this.$router.params.workspace
        },
        currentWorkspace () {
            return this.$store.getters.currentWorkspace
        }
    },
    methods: {
        ...mapActions([
            'newSession',
            'closeWorkspace'
        ]),
        updateWorkspaceName (e) {
            this.$store.commit('UPDATE_WORKSPACE_NAME', {
                workspace: this.currentWorkspace,
                name: e.target.value
            })
        }
    },
    components: {
        WorkspaceSessions
    }
}
</script>

<style lang="scss" scoped>
    input {
        background: $main-background;
        color: $white-bis;
        border: 0;
        outline: 0;
        padding: 0.5rem;
    }

    .sessions {
        margin: 2rem 0;
        flex-direction: column;
    }
</style>
