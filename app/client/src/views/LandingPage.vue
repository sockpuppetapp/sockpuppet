<template>
    <div class="container">
        <section class="hero">
            <div class="hero-body">
                <div class="container">
                    <h1 class="title has-text-centered">
                        Welcome to
                        <strong>SockPuppet</strong>
                    </h1>
                    <h2 class="subtitle has-text-centered">
                        Your websocket testing environment
                    </h2>
                </div>
            </div>
        </section>
        <div class="columns">
            <div class="column has-text-centered">
                <img src="~@/assets/logo-puppet-open-circle.png" alt="">
            </div>
            <div class="column">
                <h3 class="is-size-4 has-text-weight-semibold">Available Workspaces</h3>
                <div class="available-workspaces" v-if="workspaces.length">
                    <workspace-available-item
                        v-for="workspace in workspaces"
                        :key="workspace.id"
                        :info="workspace" />
                </div>
                <div v-else>
                    <p>Looks like you don't have any workspaces.</p>
                    <button class="button is-primary" v-on:click="newWorkspace">
                        Add new workspace
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex'
import WorkspaceAvailableItem from '@/components/structural/WorkspaceAvailableItem'

export default {
    name: 'landing-page',
    methods: {
        open (link) {
            this.$electron.shell.openExternal(link)
        },
        ...mapActions([
            'newWorkspace'
        ])
    },
    computed: {
        workspaces () {
            return this.$store.state.Workspaces.available
        }
    },
    components: {
        WorkspaceAvailableItem
    }
}
</script>

<style lang="scss" scoped>
    .title {
        color: $white-ter;

        strong {
            color: $primary;
            font-weight: 300;
        }
    }

    .subtitle {
        color: $grey-light;
    }
</style>
