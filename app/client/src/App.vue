<template>
    <div id="app">
        <navbar></navbar>
        <main class="full">
            <router-view></router-view>
        </main>
        <footer class="footer">
            <system-information></system-information>
        </footer>
    </div>
</template>

<script>
import Navbar from '@/components/structural/Navbar'
import SystemInformation from '@/components/structural/SystemInformation'

export default {
    name: 'sockpuppet',
    components: {
        Navbar,
        SystemInformation
    }
}
</script>

<style lang="scss">
    @import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro');

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    body {
        font-family: 'Source Sans Pro', sans-serif;
        overflow: hidden;
    }

    #app {
        background: $main-background;
        height: 100vh;
        padding: 0;
        width: 100vw;

        main {
            padding-top: 60px;
            height: 100vh;
        }
    }

    .full {
        display: flex;

        & > div:not(.splitter) {
            flex: 1;
        }
    }

</style>a
