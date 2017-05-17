# -*- coding: utf-8 -*-
"""
Created on Tue May  9 23:38:40 2017

@author: Carlos
"""

"""NOOOB PROJECT"""


import numpy as np
import math
import matplotlib.pyplot as plt

N=60
steps=100
Lred=math.pow(2*N,1/3)
rc=Lred/2.0
Ared=0.8
delta=1.0/2.0
tail=2.0*np.pi*Ared*0.5*math.exp(1.0-rc)
ptail=2/3*np.pi*Ared*0.5*0.5*(3+Lred/2.0)


def distance(xi,xii,yi,yii,zi,zii):
    sq1 = xi-xii-Lred*math.floor((xi-xii)/Lred+0.5)
    sq2 = yi-yii-Lred*math.floor((yi-yii)/Lred+0.5)
    sq3 = zi-zii-Lred*math.floor((zi-zii)/Lred+0.5)
    
    sq1=sq1*sq1
    sq2=sq2*sq2
    sq3=sq3*sq3  
    
    return math.sqrt(sq1 + sq2 + sq3)
    
        
r=np.zeros([N,3])


for i in range(N):
    r[i,0]=np.random.uniform()*Lred
    r[i,1]=np.random.uniform()*Lred
    r[i,2]=np.random.uniform()*Lred

E=0
Vir=0 

for i in range(N):
    for j in range(N):
        Etemp=0
        Virtemp=0
        if i<j:
            dij=distance(r[i,0],r[j,0],r[i,1],r[j,1],r[i,2],r[j,2])
            if dij<1:
                Etemp=1/math.pow(dij,3)
                Virtemp=-3*Etemp
            if dij<Lred/2:
                Etemp=1/math.pow(dij,2)*math.exp(-dij+1)
                Virtemp=-Etemp/dij-2*Etemp
        E=E+Etemp
        Vir=Vir+Virtemp
E=Ared*E
Vir=Ared*Vir

accep=0
Ener=np.zeros(steps)
Etail=np.zeros(steps)
Virial=np.zeros(steps)
Pressure=np.zeros(steps)
Ptail=np.zeros(steps)
for s in range(0,steps):
    for u in range(N):

        xnew=r[u,0]+delta*(np.random.uniform()-0.5)
        ynew=r[u,1]+delta*(np.random.uniform()-0.5)
        znew=r[u,2]+delta*(np.random.uniform()-0.5)
            
        Eij=0
        Virij=0
        for j in range(N):
            Etemp=0
            Virtemp=0
            if j!=u:
                dij=distance(r[u,0],r[j,0],r[u,1],r[j,1],r[u,2],r[j,2])
                if dij<1:
                    Etemp=1/math.pow(dij,3)
                    Virtemp=-3*Etemp
                if dij<rc:
                    Etemp=1/math.pow(dij,2)*math.exp(-dij+1)
                    Virtemp=-Etemp/dij-2*Etemp
            Eij=Eij+Etemp
            Virij=Virij+Virtemp
        Eij=Ared*Eij
        Virij=Ared*Virij
        
        
        Eijnew=0
        Virijnew=0
        for j in range(N):
            Etemp=0
            Virtemp=0
            if j!=u:
                dij=distance(xnew,r[j,0],ynew,r[j,1],znew,r[j,2])
                if dij<1:
                    Etemp=1/math.pow(dij,3)
                    Virtemp=-3*Etemp
                if dij<rc:
                    Etemp=1/math.pow(dij,2)*math.exp(-dij+1)
                    Virtemp=-Etemp/dij-2*Etemp
            Eijnew=Eijnew+Etemp
            Virijnew=Virijnew+Virtemp
        Eijnew=Ared*Eijnew
        Virijnew=Ared*Virijnew
        
        Enew=E-Eij+Eijnew
        Virnew=Vir-Virij+Virijnew
        D_E=Eijnew-Eij
        print(D_E)
        '''if D_E<=0:
            r[u,0]=xnew
            r[u,1]=ynew
            r[u,2]=znew
            E=Enew
            accep+=1
        else:'''
        '''rannum=ran.random()'''
        rannum=np.random.uniform()
        if rannum<=math.exp(-D_E):
            r[u,0]=xnew
            r[u,1]=ynew
            r[u,2]=znew
            E=Enew
            Vir=Virnew
            accep+=1            
    Ener[s]=E
    Etail[s]=Ener[s]+tail
    Virial[s]=Vir
    Pressure[s]=0.5-(1.0/(3*math.pow(Lred,3))*Virial[s])
    Ptail[s]=Pressure[s]+ptail
    
plt.plot(Ener/N)
plt.plot(Pressure)

            


  

    
    

 



    
    

           

