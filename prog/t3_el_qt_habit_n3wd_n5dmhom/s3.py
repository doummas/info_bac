from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

from pickle import *
from random import randint


def ajouter():
    
    f = open("msg.txt","a")
    ch=win.L.text()
    if ch == "" :
        QMessageBox.critical(win,"erreur","Le message est une chain invalid")
    elif espch(ch) == False:
        QMessageBox.critical(win,"erreur","Le message ne contient sue de lettre majuscule et de espaces")
    else :
        f.write(ch+"\n")
    f.close()
    
def espch(ch):
    i=0
    while i<len(ch) and ("A"<=ch[i]<="Z" or ch[i] == " "):
        i=i+1
    return i== len(ch)
        


def affich():
    f = open("msg.txt","r")
    ch=f.readline()
    while ch!="":
        win.Li.addItem(ch)
        ch=f.readline()
    f.close()
    
def cree():
    f = open("msg.txt","r")
    f1 = open("code.dat","wb")
    ch=f.readline()
    while ch!="":
        e=dict()
        e["msg1"] = esp(ch)
        ch=effacer(ch)
        while len(ch)%3!=0:
            ch= ch + chr(randint(65,90))
        msg=0
        msg2=""
        i=0
        while i<len(ch):
            
            msg=ord(ch[i+2])*ord(ch[i+1])*ord(ch[i])
            while msg>=10:
                msg=somme(msg)
            msg2=msg2+str(msg)
            i=i+3
        e["msg2"] = msg2
        dump(e,f1)
        ch=f.readline()
   
    f.close()
    f1.close()
    
    f = open("code.dat","rb")
    fin = False
    i=0
    while not fin:
        try:
            e=load(f)
            win.T.insertRow(i)
            win.T.setItem(i,0,QTableWidgetItem(e["msg1"]))
            win.T.setItem(i,1,QTableWidgetItem(e["msg2"]))
            i=i+1
        except :
            fin = not fin
    f.close()
            

def esp(ch):
    ch1=""
    for i in range(len(ch)):
        if ch[i] == " ":
            ch1 = ch1 + str(i) + "*"
    return ch1[0:len(ch1)-1]


def effacer(ch):
    ch1=""
    for i in range(len(ch)):
        if ch[i] != " ":
            ch1 =ch1 + ch[i]
    return ch1
    
    
    
def somme(msg):
    msg=str(msg)
    s=0
    for i in range(len((msg))):
        s=s+int(msg[i])
    return s
    
app = QApplication([])
win = loadUi("s3.ui")
win.show()
win.B1.clicked.connect (ajouter)
win.B3.clicked.connect (affich)
win.B2.clicked.connect (cree)

app.exec_()