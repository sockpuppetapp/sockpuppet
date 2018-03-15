<template>
    <section>
        <div class="level">
            <div class="level-item">
                <div class="field">
                    <div class="control">
                        <textarea
                            class="textarea"
                            placeholder="Message"
                            v-model="message"></textarea>
                        <button
                            class="button"
                            v-on:click="sendMessage">
                            Send
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    data () {
        return {
            message: null
        }
    },
    computed: {
        ...mapGetters([
            'currentSession'
        ])
    },
    methods: {
        sendMessage () {
            this.$store.dispatch('sendMessage', {
                session: this.currentSession,
                message: this.message
            })
        }
    }
}
</script>

<style lang="scss" scoped>
    $textarea-bg-color: rgba(255, 255, 255, 0.2%);

    .field,
    .level,
    .control,
    .level-item,
    section {
        display: flex;
        flex: 1;
        margin: 0;
        height: initial;
        align-content: stretch;
        align-items: stretch;
    }
    .textarea {
        min-width: initial !important;
        min-height: initial !important;
        max-width: initial !important;
        max-height: initial !important;
        height: initial;
        border-radius: 0;
        border: 0;
        background-color: $textarea-bg-color;
        color: $white-bis;

        &:focus,
        &:active {
            box-shadow: none !important;
            background: $textarea-bg-color !important;
            border: 0 !important;
            color: $white-bis !important;
        }
    }
    .control { position: relative; }
    .button {
        position: absolute;
        top: 0;
        right: 0;
        height: 60px;
        width: 90px;
        border-radius: 0;
        background: $main-dark;
        border-color: $main-dark;
        color: $white-bis;

        &:focus,
        &:hover,
        &:active {
            box-shadow: none !important;
            background: $main-dark;
            border-color: $main-dark;
            color: $white-bis;
        }
        &:active {
            background: $main-darker;
        }
    }

    .textarea::-webkit-input-placeholder { color: $grey-light; }
    .textarea::-moz-placeholder {color: $grey-light; }
    .textarea:-ms-input-placeholder { color: $grey-light; }
    .textarea:-o-input-placeholder { color: $grey-light; }
    .textarea::placeholder { color: $grey-light; }

</style>
