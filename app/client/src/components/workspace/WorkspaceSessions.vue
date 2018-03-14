<template>
    <ul class="workspace-sessions">
        <li
            v-for="session in sessions"
            v-on:click="setSession(session)"
            v-bind:class="sessionClass(session.id)"
            :key="session.id"
            class="pad-10">
            {{session.name}}
        </li>
    </ul>
</template>

<script>
import { mapActions } from 'vuex'
export default {
    computed: {
        sessionClass () {
            return (id) => {
                return (
                    this.currentSession &&
                    id === this.currentSession.id
                ) ? 'active' : ''
            }
        },
        currentWorkspace () {
            return this.$store.getters.currentWorkspace
        },
        currentSession () {
            return this.$store.state.Workspaces.currentSession
        },
        sessions () {
            return this.currentWorkspace.sessions
        }
    },
    methods: {
        ...mapActions([
            'setSession'
        ])
    }
}
</script>

<style lang="scss" scoped>
    $bg-color: rgba(255, 255, 255, 0.2%);

    .active {
        background: $bg-color;
    }

    .workspace-sessions li {
        cursor: pointer;
    }
</style>
