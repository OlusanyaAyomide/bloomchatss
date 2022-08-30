let send= document.getElementById('send-message')
let inputText=document.getElementById('chat-input')

inputText.addEventListener('focusin',inputTextf)
inputText.addEventListener('focusout',inputTextout)


function inputTextf(){
    document.getElementById('send-message').style.display ='block'
    document.getElementById('chat-input').style.width ='100%'
}

function inputTextout(){
    setTimeout(()=>{
        console.log('Alive')
        document.getElementById('send-message').style.display ='none'
        document.getElementById('chat-input').style.width ='60%'
    },1000)

}
function scroll(){
    window.scrollTo(0,document.body.scrollHeight)
}
history.scrollRestoration='manual'
scroll()