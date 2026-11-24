from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

from pickle import *



def ajouter():
    ch=win.L1.text()
    f=open("expression.txt","a")
    f2=open("resulat.dat","ab")
    if ch == "" or esp(ch)!=1  or (ch[0] not in ["*","+","-","/"] ) or num(ch[1:ch.find(" ")]) == False or num(ch[ch.find(" ")+1:]) == False :
        QMessageBox.critical(win,"erreur","La chaine invalid")
    elif ch[0]=="/" and ch[ch.find(" ")+1:] == "0":
        QMessageBox.critical(win,"erreur","Il faut que different de 0")
    else :
        
        f.write(ch+"\n")
        QMessageBox.critical(win,"mouch ","mrigl")
        win.L1.clear()
        
        e=dict()
        e["sym"] = ch[0]
        e["pre"] = int(ch[1:ch.find(" ")])
        e["deux"] = int(ch[ch.find(" ")+1:])
        if e["sym"] == "*":
            e["res"] = e["pre"] * e["deux"]
        elif e["sym"] == "/":
            e["res"] = e["pre"] / e["deux"]
        elif e["sym"] == "+":
            e["res"] = e["pre"] + e["deux"]
        elif e["sym"] == "-":
            e["res"] = e["pre"] - e["deux"]
        dump(e,f2)
        f2.close()
        
        f.close()
        
def num(ch):
    i=0
    while i<len(ch) and ("0"<=ch[i]<="9"):
        i=i+1
    return i == len(ch)
        
def esp(ch):
    i=0
    s=0
    while i<len(ch):
        
        if ch[i] == " ":
            s=s+1
        i=i+1
    return s


def afficher1():
    f=open("expression.txt","r")
    ch=f.readline()
    while ch!="":
        win.Li1.addItem(ch)
        ch=f.readline()
    f.close()
    

def afficher2():
    f=open("resulat.dat","rb")
    fin= False
    while not fin:
        try:
            e=load(f)
            win.Li2.addItem(str(e["res"]))
        except :
            fin = True
    f.close()
    
    
    
    
    
app = QApplication([])
win = loadUi("s1.ui")
win.show()
win.B1.clicked.connect (ajouter)
win.B2.clicked.connect (afficher1)
win.B3.clicked.connect (afficher2)




app.exec_()