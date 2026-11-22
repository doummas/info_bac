function changer(){
    document.getElementById("img1").src = Math.round(Math.random()*3+1)+".png"
    
}


function GenererCaptcha(){
    document.getElementById("captcha").value = ""
    for (let i =0;i<10;i++){
    let x = Math.round(Math.random()*25)
    if (x%2==0){
        document.getElementById("captcha").value += String.fromCharCode(x+65)
    }
    else if (x%2==1){
        document.getElementById("captcha").value += String.fromCharCode(x+97)
    }
    
    }}