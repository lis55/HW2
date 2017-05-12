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

for i in range(N):
    for j in range(N):
        if i<j:
            dij=distance(r[i,0],r[j,0],r[i,1],r[j,1],r[i,2],r[j,2])
            if dij<1:
                Etemp=Ared/(N*math.pow(dij,3))
            if dij<Lred/2:
                Etemp=Ared/(N*math.pow(dij,2))*math.exp(-dij+1)
    E=E+Etemp
    E=Ared/N*Etemp

    

    
    

 



    
    

           

