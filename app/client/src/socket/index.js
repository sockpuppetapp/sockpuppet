const onmessage = (message) => {
    console.log('onmessage', message)
    console.log('this', this)
}

const onclose = (message) => {
    console.log('onclose')
}

export {onmessage, onclose}
