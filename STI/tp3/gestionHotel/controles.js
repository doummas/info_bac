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


function captch(){
    if (document.getElementById("rep").value == maj(document.getElementById('captcha').value)){
        document.getElementById("msg").innerHTML = "Captcha valid"
    }
    else{
        document.getElementById("msg").innerHTML = "Captcha invalid"
    }
}
function maj(ch){
    s=0
    for (let i =0;i<ch.length;i++){
        if (ch[i]>="A" && ch[i]<="Z" ){
            s=s+1
        }
    }
    return s
}

function format(){
    let img = document.getElementById("im")
    img.style.width = "150px"
    img.style.height = "150px"
    img.style.borderRadius = "50%" 

}




function verif(){
    if (document.getElementById("hotel").selectedIndex == 0 || document.getElementById("hotel").selectedIndex == -1 ){
        alert("select un hotel")
        
    }
    let a = document.getElementsByName("a")
    var s=0
    for (let i =0;i<3;i++){
        if (a[i].checked){
            s=a[i].value
            
        }
    }
    if (s==0){
        alert("select acceuil")
        
    }
    let b = document.getElementsByName("b")
    var ss=0
    for (let i =0;i<3;i++){
        if (b[i].checked){
            ss=b[i].value
        }
    }
    if (ss==0){
        alert("select restaurant")}
    
    
    let c = document.getElementsByName("c")
    var sss=0
    for (let i =0;i<c.length;i++){
        if (c[i].checked){
            sss+=Number(c[i].value)
        }
    }   
    console.log(s)
    console.log(ss)

    console.log(sss)
    let ssss=Number(s) +Number(ss) +Number(sss)
    ch=""
    for(let i =0;i<ssss;i++){
        ch+="\u2605"

    }
    
    document.getElementById("msgfinal").innerHTML = "L'evaluation de 'hotel " + document.getElementById("hotel").value +"est en cour de traitemt , sa attribut est " +ch
}
