<template>
    <div class="navbar-menu">
        <div class="navbar-start workspace-selector">
            <workspace-selector-item
                v-for="workspace in workspaces"
                :key="workspace.id"
                :info="workspace" />
        </div>
        <div class="navbar-end workspace-selector">
            <workspace-add />
        </div>
    </div>
</template>

<script>
import WorkspaceSelectorItem from './WorkspaceSelectorItem'
import WorkspaceAdd from './WorkspaceAdd'

export default {
    name: 'WorkspaceSelector',
    components: {
        WorkspaceSelectorItem,
        WorkspaceAdd
    },
    computed: {
        workspaces () {
            return this.$store.state.Workspaces.available
                .filter(x => x.is_active)
        }
    }
}
</script>

<style lang="scss">
    .workspace-selector {
        margin-left: 1rem;
    }
    .workspace-selector-item {
        &.active { background: $main; }
        &:hover a { color: $dark; }
    }
    .workspace-selector-item.navbar-item {
        align-items: stretch;
        padding: 0;
        text-transform: capitalize;

        &:hover {
            background: $main-lightest;
        }
    }
    .currentWorkspace {
        display: flex;
    }
    .workspace-link {
        display: flex;
        color: $white-bis;
        align-items: center;
        padding: 0 1.25rem;
    }
</style>
