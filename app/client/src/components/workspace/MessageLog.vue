<template>
    <section>
        <div class="level">
            <div class="level-left">
                <div class="level-item">
                    <h2 class="is-size-4">Log</h2>
                </div>
            </div>
        </div>
        <div class="level log-level">
            <div class="level-left">
                <div class="level-item">
                    <ul class='message-log'>
                        <message
                            v-for="message in currentSessionLog"
                            v-bind:info="message"
                            :key="message.id"/>
                    </ul>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import { mapGetters } from 'vuex'
import Message from '@/components/workspace/Message'

export default {
    computed: {
        ...mapGetters([
            'currentSession',
            'currentSessionLog'
        ])
    },
    components: { Message }
}
</script>

<style scoped>
    ul,
    .field,
    .level-item,
    .log-level,
    .log-level .level-left,
    .message-log,
    section {
        display: flex;
        flex: 1;
        margin: 0;
        height: initial;
        align-content: stretch;
        align-items: stretch;
    }
    ul,
    section {
        flex-direction: column;
    }

    .message-log {
        overflow-y: auto;
    }
</style>
