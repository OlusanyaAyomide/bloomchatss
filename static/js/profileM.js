let roomButton=document.getElementById('room-button')
let commentButton=document.getElementById('comment-button')

roomButton.addEventListener('click',handleClickroom)
commentButton.addEventListener('click',handleClickcomment)

function handleClickroom(){
        document.getElementById('rooms').style.display = 'block'
        document.getElementById('comments').style.display = 'none'
        document.getElementById('comment-button').style.backgroundColor = 'transparent'
        document.getElementById('room-button').style.backgroundColor = 'white'
}
function handleClickcomment(){
    document.getElementById('comments').style.display = 'block'
    document.getElementById('rooms').style.display = 'none'
    document.getElementById('room-button').style.backgroundColor = 'transparent'
    document.getElementById('comment-button').style.backgroundColor = 'white'
}