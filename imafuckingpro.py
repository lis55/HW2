# -*- coding: utf-8 -*-
"""
Created on Mon May 15 18:16:32 2017

@author: Carlos
"""

import numpy as np
import math
import matplotlib.pyplot as plt

N=60
steps=100
Lred=math.pow(2.0*N,1/3)
rc=Lred/2
Ared=0.8
delta=1.0/4.0
tail=2.0*np.pi*Ared*0.5*math.exp(1.0-rc)
ptail=2/3*np.pi*Ared*0.5*0.5*(3+Lred/2.0)

accep=0
Ener=np.zeros(steps)
Etail=np.zeros(steps)
Virial=np.zeros(steps)
Pressure=np.zeros(steps)
Ptail=np.zeros(steps)
conftest=np.array([[1,0,0],[2,0,0]])

def distance(conf,k,u):
    sq1 = conf[k,0]-conf[u,0]-Lred*math.floor((conf[k,0]-conf[u,0])/Lred+0.5)
    sq2 = conf[k,1]-conf[u,1]-Lred*math.floor((conf[k,1]-conf[u,1])/Lred+0.5)
    sq3 = conf[k,2]-conf[u,2]-Lred*math.floor((conf[k,2]-conf[u,2])/Lred+0.5)
    
    sq1=sq1*sq1
    sq2=sq2*sq2
    sq3=sq3*sq3  
    
    return math.sqrt(sq1 + sq2 + sq3)

def totalenergy(conf):
    E=0
    Vir=0
    for i in range(N):
        for j in range(N):
            Etemp=0
            Virtemp=0
            if i<j:
                dij=distance(conf,i,j)
                if dij<1:
                    Etemp=1/math.pow(dij,3)
                    Virtemp=-3*Etemp
                if dij<rc:
                    Etemp=1/math.pow(dij,2)*math.exp(-dij+1)
                    Virtemp=-Etemp/dij-2*Etemp
            E+=Etemp
            Vir+=Virtemp
    E=Ared*E
    Vir=Ared*Vir
    return np.array([E,Vir])
    
def energyi(conf,i):
    Eij=0
    Virij=0
    for j in range(N):
        Etemp=0
        Virtemp=0
        if j!=i:
            dij=distance(conf,i,j)
            if dij<1:
                Etemp=1/math.pow(dij,3)
                Virtemp=-3*Etemp
            if dij<rc:
                Etemp=1/math.pow(dij,2)*math.exp(-dij+1)
                Virtemp=-Etemp/dij-2*Etemp
        Eij+=Etemp
        Virij+=Virij+Virtemp
    Eij=Ared*Eij
    Virij=Ared*Virij
    
    return np.array([Eij,Virij])

r=np.zeros([N,3])
rnew=np.zeros([N,3])
for i in range(N):
    r[i,0]=np.random.uniform()*Lred
    r[i,1]=np.random.uniform()*Lred
    r[i,2]=np.random.uniform()*Lred

Energy=np.zeros(steps)
Virial=np.zeros(steps)
Pressure=np.zeros(steps)
Resultsrun=totalenergy(r)
for f in range(N):
    rnew[f,0]=r[f,0]
    rnew[f,1]=r[f,1]
    rnew[f,2]=r[f,2]
D_E=np.zeros(2) 


for s in range(0,steps):
    for l in range(N):
        rnew[l,0]=r[l,0]+delta*(np.random.uniform()-0.5)
        rnew[l,1]=r[l,1]+delta*(np.random.uniform()-0.5)
        rnew[l,2]=r[l,2]+delta*(np.random.uniform()-0.5)
        
        D_Results=energyi(rnew,l)-energyi(r,l)

        rannum=np.random.uniform()
        if rannum<=math.exp(-D_Results[0]):

            r[l,0]=rnew[l,0]
            r[l,1]=rnew[l,1]
            r[l,2]=rnew[l,2]
            Resultsrun+=D_Results
            accep+=1              
            
    Energy[s]=Resultsrun[0]
    Virial[s]=Resultsrun[1]

TotalEnergy=np.mean(Energy)/N
plt.plot(Energy/N)        
'''if rannum<=math.exp(-D_Results[0]):'''        
    





    
            