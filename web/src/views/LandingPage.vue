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
                Second column
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'landing-page',
    methods: {
        open (link) {
            this.$electron.shell.openExternal(link)
        }
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
