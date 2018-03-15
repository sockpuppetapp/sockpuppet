<template>
    <section>
        <div class="level"
            v-bind:class="statusClass">
            <div class="level-left">
                <div class="level-item">
                    <div class="field">
                        <div class="control has-icons-left">
                            <span class="icon is-medium dark" v-if="status === 0">
                                <circle-outline-icon />
                            </span>
                            <span class="icon is-medium danger" v-if="status === 1">
                                <alert-circle-outline-icon />
                            </span>
                            <span class="icon is-medium warning" v-if="status === 2">
                                <circle-outline-icon />
                            </span>
                            <span class="icon is-medium success" v-if="status === 3">
                                <circle-icon />
                            </span>
                            <input
                                class="input"
                                type="text"
                                placeholder="ws://localhost/myfeed"
                                v-bind:value="currentSession.location"
                                @input="updateSession"
                                :disabled="status > 1" />
                        </div>
                    </div>
                </div>
            </div>
            <div class="level-right">
                <div class="level-item">
                    <button class="button" v-on:click="connect">{{buttonText}}</button>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import { mapGetters } from 'vuex'
import CircleIcon from 'mdi-vue/CircleIcon'
import CircleOutlineIcon from 'mdi-vue/CircleOutlineIcon'
import AlertCircleOutlineIcon from 'mdi-vue/AlertCircleOutlineIcon'

const statuses = [
    {
        class: '',
        text: 'Connect'
    },
    {
        class: 'was-error',
        text: 'Connect'
    },
    {
        class: 'in-progress',
        text: 'Waiting'
    },
    {
        class: 'is-connected',
        text: 'Close'
    }
]
// STATUSES:
// 0: Not Connected
// 1: Error
// 2: In progress
// 3: Connected
export default {
    computed: {
        status () {
            return this.currentWorkspace.status || 0
        },
        buttonText () {
            return statuses[this.status].text
        },
        statusClass () {
            return statuses[this.status].class
        },
        ...mapGetters([
            'currentWorkspace',
            'currentSession'
        ])
    },
    methods: {
        connect () {
            this.$store.commit('NEW_SOCKET', this.currentWorkspace)

            // TODO:
            // - Check status and assign appropriately
            let status = 3
            // let status = this.status + 1
            // if (status > 3) { status = 0 }
            this.$store.commit('SET_STATUS', {
                workspace: this.currentWorkspace,
                status: status
            })
        },
        updateSession (e) {
            this.$store.commit('UPDATE_SESSION_URL', {
                session: this.currentSession,
                location: e.target.value
            })
        }
    },
    components: {
        CircleIcon,
        CircleOutlineIcon,
        AlertCircleOutlineIcon
    }
}
</script>

<style lang="scss" scoped>
    .level {
        align-items: stretch;

    }
    .level-left {
        flex: 1;

        .field,
        .level-item { flex-grow: 1; }
    }
    .field,
    .control,
    .level-item,
    .level-left,
    .level-right,
    .location-input {
        display: flex;
        align-items: stretch;
    }
    .input {
        height: initial;
        background: rgba(255, 255, 255, 0.9%);
        border-radius: 0;
        &:focus {
            border-color: initial;
            box-shadow: none;
        }
    }
    .field,
    .button {
        height: initial;
        border-radius: 0;
        background: $main-light;
        border-color: $main-light;
        color: $white-bis;
        width: 90px;

        &:focus,
        &:hover,
        &:active {
            box-shadow: none !important;
            background: $main-light;
            border-color: $main-light;
            color: $white-bis;
        }
    }
    .control {
        flex: 1;
        &.is-connected {
            border-color: $success;
        }
        .icon {
            bottom: 0;
            margin: auto;
        }
    }
    .is-connected {
        .input {
            border-color: $success;
            color: $success;
        }
        .button {
            border-color: $success;
            background: $success;
        }
    }
    .in-progress {
        .input {
            border-color: $warning;
            color: $warning;
        }
        .button {
            border-color: $warning;
            background: $warning;
        }
    }
    .was-error {
        .input {
            border-color: $danger;
            color: $danger;
        }
        .button {
            border-color: $danger;
            background: $danger;
        }
    }
</style>
