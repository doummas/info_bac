from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

from pickle import *



def ajouter():
    f= open("client.dat","ab")
    ch1=win.L1.text()
    ch2=win.L2.text()
    r1 = win.R1.isChecked()
    r2 = win.R2.isChecked()
    if ch1 == "" or ch2=="":
        QMessageBox.critical(win,"erreur","Veuillez saisir des information")
    elif not chnum(ch1):
        QMessageBox.critical(win,"erreur","L'indentifiant invalid")
    elif len(ch2)!=8:
        QMessageBox.critical(win,"erreur","N*telphone invalid")
    else:
        e=dict()
        e["cin"] = ch1
        e["tel"] = ch2
        e["ville"] = win.C.currentText()
        if r1:
            e["genre"] = "Masculin"
        elif r2:
            e["genre"] = "Feminin"
        if win.chh.isChecked():
            e["etat"] = "Inscrit"
        else :
            e["etat"] = "Non inscrit"
        dump(e,f)
    f.close()
        
def chnum(ch):
    i=0
    while i<len(ch) and ("0"<=ch[i]<="9" or ch[i]=="C"):
        i=i+1
    return i== len(ch)





def affclient():
    f= open("client.dat","rb")
    fin = False
    i=0
    while not fin:
        try:
            e=load(f)
            win.T.insertRow(i)
            win.T.setItem(i,0,QTableWidgetItem(e["cin"]))
            win.T.setItem(i,1,QTableWidgetItem(e["tel"]))
            win.T.setItem(i,2,QTableWidgetItem(e["ville"]))
            win.T.setItem(i,3,QTableWidgetItem(e["genre"]))
            win.T.setItem(i,4,QTableWidgetItem(e["etat"]))
            i=i+1
        except :
            fin = True
    f.close()
            
    
    
def affgagants():
    win.Li.clear()
    f= open("client.dat","rb")
    fin = False
    while not fin:
        try :
            e=load(f)
            a= e["tel"]
            while len(str(a))>1:
                a=str(somme(a))
            if int(a) %2==0:
                win.Li.addItem((e["tel"]))
        except:
            fin = True
    f.close()
    
    
    
def somme(ch):
    s=0
    for i in range(len(ch)):
        s=s+int(ch[i])
    return s
    
    
    

app = QApplication([])
win = loadUi("s2.ui")
win.show()
win.B1.clicked.connect (ajouter)
win.B2.clicked.connect (affclient)
win.B3.clicked.connect (affgagants)
app.exec_()
