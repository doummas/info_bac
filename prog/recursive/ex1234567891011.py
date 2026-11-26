from numpy import *

#1
def pgcd(a,b):
        if b==0:
            return a
        else :
            return pgcd(b,a%b)
        
        


#yitgyuitiuttuytyt

#2
def chaine(ch):
    if len(ch)<1:
        return ""
    else:
        return ch[len(ch)-1] + chaine(ch[:len(ch)-1])
    




#3
def chercher(ch,c):
    if ch[0] == c:
        return True
    elif len(ch)==1:
        return c==ch[0]
    else:
        return chercher(ch[1:],c)
    


#4
def chercher_ent(ch,c):
    if ch == 0:
        return False
    elif ch//(puis(str(ch)))==c:
        return True
    else :
        return chercher_ent(ch%(puis(str(ch))),c)
        
def puis(ch):
    s=1
    for i in range (len(ch)-1):
        s*=10
    return s

#5
def palin(ch):
    if len(ch)<=1:
        return True
    elif ch[0] != ch[len(ch)-1]:
        return False
    else :
        return palin(ch[1:len(ch)-1])
    

         

#6
"""def puiss_rec(b,a,n):
    if n==0:
        return a//b
    else:
        return puiss_rec(b,b*a,n-1)
        
        
print(puiss_rec(5,5,3))"""


def puiss_rec(a,n):
    if n==0:
        return 1
    else:
        return a*puiss_rec(a,n-1)
print(puiss_rec(5,3))    
#7
from math import *
def puiss_reel(a,n):
    if n==0:
        return 1
    else :
        if n<0:
            
            return 1/a*((puiss_reel(a,n+1)))
        else :
            return a*((puiss_reel(a,n-1)))
        
print(puiss_reel(10,-2))
    

#8  
    
def rec_t(T,n,x):
    if n==-1:
        return 0
    elif x == T[n]:
        return 1 +rec_t(T,n-1,x)
    else:
        return rec_t(T,n-1,x)
print(rec_t([5,5,9,5],3,5))




#9
def recherch(T,n,x):
    if n==-1:
        return False
    elif x == T[n]:
        return True
    else:
        return recherch(T,n-1,x)
    
    
print(recherch([7,7,9,7],3,9))





#10

def t_pal(T,n,i):
    if n==0:
        return True
    else:
        if T[n] == T[i]:
            return  t_pal(T,n-1,i+1)
        else :
            return False
        
        
        
        
print(t_pal([7,8,8,7],3,0))




#11