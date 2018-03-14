const onmessage = (message) => {
    console.log('onmessage', message)
}

const onclose = (message) => {
    console.log('onclose')
}

export {onmessage, onclose}
