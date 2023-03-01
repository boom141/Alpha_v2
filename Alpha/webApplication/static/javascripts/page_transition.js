
const page_btn = document.querySelectorAll('.page-btn')
const form_img = document.getElementsByClassName('form-img')
document.getElementById('new-session').addEventListener('click', ()=>{
   document.getElementById('page-mode').innerText = 'New'
   document.getElementsByName('room-name')[0].placeholder = 'Room Name'
   $(form_img[1]).hide('fast', function(){ $(form_img[0]).show('fast') })

   $(page_btn[0]).css({'display':'flex'})

   $('.page-transition').show('fast', function(){
        $('.transition-container').animate({marginTop: '3rem'},500)
   })
})

document.getElementById('join-session').addEventListener('click', ()=>{
   document.getElementById('page-mode').innerText = 'Join'
   document.getElementsByName('room-name')[0].placeholder = 'Room Code'
   $(form_img[0]).hide('fast', function(){ $(form_img[1]).show('fast') })
   $(page_btn[1]).css({'display':'flex'})

   $('.page-transition').show('fast', function(){
        $('.transition-container').animate({marginTop: '3rem'},500)
   })
})

document.getElementById('cancel-btn').addEventListener('click', ()=>{
    $('.transition-container').animate({marginTop: '-100rem'},500,function(){
        $('.page-transition').hide('fast')
        page_btn.forEach(element => {
            $(element).hide('fast')
        });
    })

})

const new_room = () =>{
    // window.location.href = 'webApplication/pages/lobby.html'
}

const join_room = () =>{
    alert('join room')
}