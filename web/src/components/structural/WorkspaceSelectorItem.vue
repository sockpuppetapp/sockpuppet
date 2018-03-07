<template>
    <div class="workspace-selector-item navbar-item">
        <router-link :to="route" class="workspace-link">{{info.name}}</router-link>
    </div>
</template>

<script>
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
    }
}
</script>
