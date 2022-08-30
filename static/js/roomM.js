let send= document.getElementById('send-message')
let inputText=document.getElementById('chat-input')
let back=document.getElementById('room-back')
let to_desc=document.getElementById('chat-desc')
try{
    inputText.addEventListener('focusin',inputTextf)
    inputText.addEventListener('focusout',inputTextout)
}
catch(err){}
back.addEventListener('click',handleback)
to_desc.addEventListener('click',handleback)
window.addEventListener('resize',handleChange)

function inputTextf(){
    document.getElementById('send-message').style.display ='block'
    document.getElementById('chat-input').style.width ='100%'
}

function inputTextout(){
    setTimeout(()=>{
        document.getElementById('send-message').style.display ='none'
        document.getElementById('chat-input').style.width ='60%'
    },1000)
}
function handleback(){
    if (window.innerWidth > 1100){}
    else{
        if(document.getElementById('chat-div').style.display==='none'){
            document.getElementById('chat-div').style.display='block' 
            document.getElementById('description-div').style.display='none' 
        }
        else{
            document.getElementById('description-div').style.display='block' 
            document.getElementById('chat-div').style.display='none'    
        }
    }
}
function handleChange(){
    if(window.innerWidth > 1100){
        document.getElementById('description-div').style.display='block'
        document.getElementById('chat-div').style.display='block'
    }
    else if(window.innerWidth > 850 || window.innerWidth < 1100){
        console.log('here')
        document.getElementById('description-div').style.display='none' 
    }
}
function scroll(){
    window.scrollTo(0,document.body.scrollHeight)
}
history.scrollRestoration='manual'
scroll()