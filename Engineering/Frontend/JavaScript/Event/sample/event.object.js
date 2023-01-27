
let element = document.getElementById('root')
element.innerHTML = "<input type='button' value='B U T T O N'></input>"

let text = document.getElementById('event')

let eventHandler = (event) => {
    switch(event.type) {
        case 'click':
            text.textContent = 'You clicked!';
            break;
        case 'mousemove':
            text.textContent = 'You moved a mouse!';
            break;
    }
}

element.addEventListener('click', eventHandler)