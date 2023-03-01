
// established connection to server
const socket = io(window.origin + '/lobby')

const room_name = document.getElementById('room-name').innerText.split(':')[1].split(' ')[1]

socket.on('player_joined', (data)=>{
    const usernames = document.querySelectorAll('.player-username')
    const player_icons = document.querySelectorAll('.player-ico')

    data[room_name]['players'].forEach((username,index) => {
        player_icons[index].src = '/static/images/p-active.png'
        usernames[index].innerText = username
    });
        
    const player_count = document.getElementById('player-count').innerText = `Session Players: ${data[room_name]['players'].length} / 2`

})


socket.on('item_manager', (data) =>{
    return
})


const create_item = (item_name) =>{
    return `<div class="per-item">
                <h2 class="base-color">${item_name}</h2>
                <img onclick="delete_item()" src="https://img.icons8.com/external-neu-royyan-wijaya/32/F9A826/external-bin-neu-interface-neu-royyan-wijaya-2.png"/>
            </div>`
}

let room_item_list = []
const add_item = () =>{
    const item = document.getElementById('item')
    socket.emit('item_manager', room_item_list)

    item.value = ''
}