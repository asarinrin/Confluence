console.log("this is sample")

let root = document.getElementById('root')
let parent = document.getElementById('parent')
let child = document.getElementById('child')

let eventHandler = (event) => {
    console.log(event.target.tagName)
    console.log(event.currentTarget.tagName)
}

root.addEventListener('click', eventHandler, true)
root.addEventListener('click', eventHandler)
parent.addEventListener('click', eventHandler)
child.addEventListener('click', eventHandler)