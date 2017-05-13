# -*- coding: utf-8 -*-
"""
Created on Sat May 13 18:07:42 2017

@author: Carlos
"""
import random as ran
import numpy as np
import math
import matplotlib.pyplot as plt

N=60
steps=100
Lred=math.pow(2.0*N,1/3)
Ared=0.8
delta=1.0/4.0
def distance(xi,xii,yi,yii,zi,zii):
    sq1 = xi-xii-Lred*math.floor((xi-xii)/Lred+0.5)
    sq2 = yi-yii-Lred*math.floor((yi-yii)/Lred+0.5)
    sq3 = zi-zii-Lred*math.floor((zi-zii)/Lred+0.5)
    
    sq1=sq1*sq1
    sq2=sq2*sq2
    sq3=sq3*sq3  
    
    return math.sqrt(sq1 + sq2 + sq3)
    
def totalenergy(pos):
    Etemp=0
    E=0
    for i in range(N):
        for j in range(N):
            Etemp=0
            if i<j:
                dij=distance(pos[i,0],pos[j,0],pos[i,1],pos[j,1],pos[i,2],pos[j,2])
                if dij<1:
                    Etemp=1/math.pow(dij,3)
                if dij<Lred/2:
                    Etemp=1/math.pow(dij,2)*math.exp(-dij+1)
            E=E+Etemp
    E=Ared*E
    return E
    
'''energy of the u particle'''    
def energy_i(pos,u):
    Etemp=0
    E=0
    for j in range(N):
        Etemp=0
        if j!=u:
            dij=distance(pos[u,0],pos[j,0],pos[u,1],pos[j,1],pos[u,2],pos[j,2])
            if dij<1:
                Etemp=1/math.pow(dij,3)
            if dij<Lred/2:
                Etemp=1/math.pow(dij,2)*math.exp(-dij+1)
        E=E+Etemp
    E=Ared*E
    return E
    
'''Generate random positions'''
r=np.zeros([N,3])
for i in range(N):
    r[i,0]=ran.random()*Lred
    r[i,1]=ran.random()*Lred
    r[i,2]=ran.random()*Lred 

'''initial energy'''
Energy=np.zeros(steps)
Erun=totalenergy(r)
'''MC cycles'''
accep=0
rnew=np.zeros([N,3]) 

for i in range(N):
    rnew[i,0]=r[i,0]
    rnew[i,1]=r[i,1]
    rnew[i,2]=r[i,2]

for s in range(steps):

    for k in range (N):
        xnew=r[k,0]+delta*(ran.random()-0.5)
        ynew=r[k,1]+delta*(ran.random()-0.5)
        znew=r[k,2]+delta*(ran.random()-0.5)
        rnew[k,0]=xnew
        rnew[k,1]=ynew
        rnew[k,2]=znew
        
        '''D_E=energy_i(rnew,k)-energy_i(r,k)'''
        Eiold=energy_i(r,k)
        Einew=energy_i(rnew,k)
        D_E=Einew-Eiold
        Enew=Erun-Eiold+Einew
        print(D_E)
        
        '''if D_E<=0:
            r[:][:]=rnew[:][:]
            Erun=Enew
            accep+=1
        else:'''
        rannum=ran.random()
        if rannum<=math.exp(-D_E):
            r[k,0]=xnew
            r[k,1]=ynew
            r[k,2]=znew
            Erun=Enew
            accep+=1
                
    Energy[s]=Erun/N
plt.plot(Energy)


        
        
        
    
