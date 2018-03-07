<template>
    <div class="workspace-add workspace-selector-item navbar-item">
        <a v-on:click="newWorkspace" class="workspace-link narrow">
            <span class="icon is-large white">
                <plus-icon />
            </span>
        </a>
    </div>
</template>

<script>
import { mapActions } from 'vuex'
import PlusIcon from 'mdi-vue/PlusIcon'

export default {
    methods: {
        ...mapActions([
            'newWorkspace'
        ])
    },
    components: {
        PlusIcon
    }
}
</script>

<style scoped>
    .workspace-link.narrow {
        padding-left: .15rem;
        padding-right: .15rem;
    }
</style>
