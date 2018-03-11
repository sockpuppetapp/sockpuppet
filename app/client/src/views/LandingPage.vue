<template>
    <div class="container">
        <section class="hero">
            <div class="hero-body">
                <div class="container">
                    <h1 class="title">
                        Welcome to
                        <strong>SockPuppet</strong>
                    </h1>
                    <h2 class="subtitle">
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
                <h3>Open Available Workspace</h3>
                <workspace-available-item
                    v-for="workspace in workspaces"
                    :key="workspace.id"
                    :info="workspace" />
            </div>
        </div>
    </div>
</template>

<script>
import WorkspaceAvailableItem from '@/components/structural/WorkspaceAvailableItem'

export default {
    name: 'landing-page',
    methods: {
        open (link) {
            this.$electron.shell.openExternal(link)
        }
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
