let search=document.getElementById('search')
let notification=document.getElementById('notification')
let home = document.getElementById('home')
let dm= document.getElementById('dm')
let room_search= document.getElementById('search-room')
let recent= document.getElementById('recent')
let trending=document.getElementsByClassName('search-trending')

console.log('Alive')
search.addEventListener('click',searchf)
try{
    notification.addEventListener('click',notificationf)
}
catch(err){}
home.addEventListener('click',homef)
try{
    dm.addEventListener('click',dmf)
}
catch(err){}
room_search.addEventListener('focusin',resize_search)
room_search.addEventListener('focusout',undo_resize)
try{
    recent.addEventListener('click',recentf)
}
catch(err){}
for (let i of trending){
    i.addEventListener('click',homef)
}
let check = document.getElementById('check')
if (check.innerHTML === 'Yes'){
    homef()
}
function determine(num){
    if (window.innerWidth>1100){
        document.getElementById('search-div').style.display = 'block'        
    }
    else{
        if (num){
            document.getElementById('search-div').style.display = 'block'    
        }
        else{
            document.getElementById('search-div').style.display = 'none'    
        }
    }
}
function searchf(){
    document.getElementById('notification-div').style.display='none'
    document.getElementById('dm-div').style.display='none'
    determine(true)
    document.getElementById('room-list-div').style.display='none'
    document.getElementById('recent-div').style.display='none'
}


function notificationf(){
    document.getElementById('notification-div').style.display='block'
    document.getElementById('dm-div').style.display='none'
    determine(false)
    document.getElementById('room-list-div').style.display='none'
    document.getElementById('recent-div').style.display='none'
}

function homef(){
    document.getElementById('notification-div').style.display='none'
    document.getElementById('dm-div').style.display='none'
    determine(false)
    document.getElementById('room-list-div').style.display='block'
    document.getElementById('recent-div').style.display='none'
    
}
function dmf(){
    document.getElementById('notification-div').style.display='none'
    document.getElementById('dm-div').style.display='block'
    determine(false)
    document.getElementById('room-list-div').style.display='none'
    document.getElementById('recent-div').style.display='none'
}
function recentf(){
    document.getElementById('notification-div').style.display='none'
    document.getElementById('dm-div').style.display='none'
    determine(false)
    document.getElementById('room-list-div').style.display='none'
    document.getElementById('recent-div').style.display='block'
}
function resize_search(){
    document.getElementById('search-room').style.width='75vw'
}
function undo_resize(){
    setTimeout(()=>{
    document.getElementById('search-room').style.width='60vw'
},1000)
}
window.addEventListener('resize',()=>{
    if (window.innerWidth > 1100){
        document.getElementById('search-div').style.display='block'

    }
    else if(window.innerWidth > 800 && window.innerWidth<1100){
        document.getElementById('search-div').style.display='none'
    }
})
