# -*- coding: utf-8 -*-
"""
Created on Tue May  9 23:38:40 2017

@author: Carlos
"""

"""NOOOB PROJECT"""

import random as ran
import numpy as np
import math

N=10
Lred=math.pow(N/0.5,1/3)
Ared=0.8
delta=1/4
def distance(xi,xii,yi,yii,zi,zii):
    sq1 = xi-xii-Lred*math.floor((xi-xii)/Lred)
    sq2 = yi-yii-Lred*math.floor((yi-yii)/Lred)
    sq3 = zi-zii-Lred*math.floor((zi-zii)/Lred)
    
    sq1=sq1*sq1
    sq2=sq2*sq2
    sq3=sq3*sq3  
    
    return math.sqrt(sq1 + sq2 + sq3)
    
        

r=np.zeros([N,3])
for i in range(N):
    r[i,0]=ran.random()
    r[i,1]=ran.random()
    r[i,2]=ran.random()

steps=100
for s in range (0,steps):
    E=0
    
    
    for i in range(N):
        for j in range(N):
            Etemp=0
            if i<j:
                dij=distance(r[i,0],r[j,0],r[i,1],r[j,1],r[i,2],r[j,2])
                if dij<1:
                    Etemp=Ared/(N*math.pow(dij,3))
                if dij<Lred/2:
                    Etemp=Ared/(N*math.pow(dij,2))*math.exp(-dij+1)
            E=E+Etemp
    E=Ared/N*E
    
    
    u=int(ran.random()*N)
    xnew=r[u,0]+delta*(ran.random()-0.5)
    ynew=r[u,1]+delta*(ran.random()-0.5)
    znew=r[u,2]+delta*(ran.random()-0.5)
    
    Eij=0
    for j in range(N):
        Etemp=0
        if u<j:
            dij=distance(r[u,0],r[j,0],r[u,1],r[j,1],r[u,2],r[j,2])
            if dij<1:
                Etemp=Ared/(N*math.pow(dij,3))
            if dij<Lred/2:
                Etemp=Ared/(N*math.pow(dij,2))*math.exp(-dij+1)
        Eij=Eij+Etemp
    Eij=Ared/N*E
    
    Eijnew=0
    for j in range(N):
        Etemp=0
        if u<j:
            dij=distance(xnew,r[j,0],ynew,r[j,1],znew,r[j,2])
            if dij<1:
                Etemp=Ared/(N*math.pow(dij,3))
            if dij<Lred/2:
                Etemp=Ared/(N*math.pow(dij,2))*math.exp(-dij+1)
        Eijnew=Eijnew+Etemp
    Eijnew=Ared/N*E
    
    Enew=E-Eij+Eijnew
    D_E=Enew-E
    
    if D_E<=0:
        r[i,0]=xnew
        r[i,1]=ynew
        r[i,2]=znew
    else:
        ran=ran.random()
        if ran<=math.exp(-D_E):
            r[i,0]=xnew
            r[i,1]=ynew
            r[i,2]=znew

            


  

    
    

 



    
    

           

