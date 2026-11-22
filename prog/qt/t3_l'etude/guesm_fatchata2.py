from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from pickle import *
from random import randint



def ajouter():
    ch = win.L1.text()
    f = open("msg.txt","a")
    if ch == "":
        QMessageBox.critical(win,"erreur","Le message du chaine est non vide")
    elif maj(ch)==False:
        QMessageBox.critical(win,"erreur","Le message ne contient que lltre majuscule et espace")

    else :
        f.write(ch)
        
def maj(ch):
    i=0
    while i<len(ch) and ("A"<=ch[i]<="Z" or ch[i]==" "):
        i+=1
    return i==len(ch)


def afficher():
    f = open("msg.txt","r")
    win.Li1.addItem(f.read())

def cree():
    f = open("msg.txt","r")
    f1 = open("code.dat","wb")
    ch=f.readline()
    while ch!="":
        
        msg1=pos(ch)
        msg=effacer(ch)
        while len(msg)%3!=0:
            msg+=chr(randint(65,90))
        e=dict()
        msg2=""
        for i in range(1,len(msg),3):
            a=str(ord(msg[i-1])*ord(msg[i])*ord(msg[i+1]))
            
            while len(a)>1:
                b=0
                for j in range(len(a)):
                    b+=int(a[j])
                a=str(b)
                
                
            msg2+=a
        e["msg2"] = msg2
        e["msg1"]=msg1
        dump(e,f1)
        
        ch=f.readline()
    f1.close()
    f.close()
        
    f2 = open("code.dat","rb")    
    fin = False
    i=0
    while not fin:
        try:
            e=load(f2)
            win.T.insertRow(i)
            win.T.setItem(i,0,QTableWidgetItem(str(e["msg1"])))
            win.T.setItem(i,1,QTableWidgetItem(str(e["msg2"])))
            i+=1
        except:
            fin=True
    f2.close()
def pos(ch):
    s=""
    for i in range(len(ch)):
        if ch[i] == " ":
            s+=str(i)+"*"
    return s[0:len(s)-1]


def effacer(ch):
    while ch.find(" ")!=-1:
        i=ch.find(" ")
        ch=ch[0:i]+ch[i+1:]
        
    return ch
   


app = QApplication([])
win = loadUi("interface.ui")
win.show()
win.B1.clicked.connect (ajouter)
win.b2.clicked.connect(afficher)
win.B3.clicked.connect(cree)
app.exec_()