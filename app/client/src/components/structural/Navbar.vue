<template>
    <nav class="navbar is-fixed-top" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <router-link to="/">
                <img id="logo" src="~@/assets/logo-words.png">
            </router-link>
        </div>
        <workspace-selector />
    </nav>
</template>

<script>
import WorkspaceSelector from './WorkspaceSelector'

export default {
    name: 'Navbar',
    components: {
        WorkspaceSelector
    }
}
</script>
