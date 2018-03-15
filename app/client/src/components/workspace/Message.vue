<template>
    <li class="box breathe-r-20 msg">
        <div class="level">
            <div class="level-left">
                <div class="level-item text">
                    {{info.message}}
                </div>
            </div>
            <div class="level-right">
                <div class="level-item">
                    <label class="tag" v-bind:class="info.direction.toLowerCase()">
                        {{info.direction}}
                    </label>
                </div>
            </div>
        </div>
        <div class="level">
            <div class="level-left">
                <div class="level-item">
                    <small>
                        {{info.created}}
                    </small>
                </div>
            </div>
        </div>
    </li>
</template>

<script>
export default {
    props: ['info']
}
</script>

<style lang="scss" scoped>
    .msg {
        .level-left,
        .level-right,
        .level {
            margin: 0;
            height: initial;
        }
        label {
            &.outgoing {
                background-color: $main;
                color: findColorInvert($main);
            }
            &.incoming {
                background-color: $primary;
                color: findColorInvert($primary);
            }
        }
        small {
            color: rgba($white, 0.3%);
        }
        .text {
            font-family: monospace;
        }
    }
</style>
