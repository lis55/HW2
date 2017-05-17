# -*- coding: utf-8 -*-
"""
Created on Wed May 17 13:20:33 2017

@author: Carlos
"""

import numpy as np
import math
import matplotlib.pyplot as plt

def blocking(u, M):
	N=len(u)
	n=int(math.floor(N/(1.0*M)))
	g_temp=np.zeros(n)
	U=np.zeros(n)

	unerror_u=np.sqrt(1.0/N*np.var(u))

	print (unerror_u)

	for i in range(0,n):
	    ji=i*M
	    jf=(i+1)*M-1
	    
	    for j in range(ji,jf+1):
             g_temp[i]=g_temp[i]+u[j]
	
	    U[i]=1.0/M*g_temp[i]

	return U

FILEdata1 = open("Energy3.txt","r") 
FILEdata2 = open("Energy4.txt","r")
FILEdata3 = open("Energy5.txt","r")
FILEdata4 = open("Energy6.txt","r")
'''FILEdata5 = open("energy5.txt","r")
FILEdata6 = open("energy6.txt","r")'''
data1 = np.loadtxt(FILEdata1)
data2 = np.loadtxt(FILEdata2)
data3 = np.loadtxt(FILEdata3)
data4 = np.loadtxt(FILEdata4)
'''data5 = np.loadtxt(FILEdata5)
data6 = np.loadtxt(FILEdata6)'''


u1=data1
u2=data2
u3=data3
u4=data4

'''
N=len(u1)
C1=np.zeros(N)
C2=np.zeros(N)
C3=np.zeros(N)
C4=np.zeros(N)
for n in range (0,1):
    for k in range(0,N-n):
        C1[n]=C1[n]+((u1[k+n]-np.mean(u1))*(u1[k]-np.mean(u1)))
        C2[n]=C2[n]+((u1[k+n]-np.mean(u2))*(u2[k]-np.mean(u2)))
        C3[n]=C3[n]+((u1[k+n]-np.mean(u3))*(u3[k]-np.mean(u3)))
        C4[n]=C4[n]+((u1[k+n]-np.mean(u4))*(u4[k]-np.mean(u4)))
       
    C1[n]=(1.0/(N-n))*C1[n]
    C2[n]=(1.0/(N-n))*C2[n]
    C3[n]=(1.0/(N-n))*C3[n]
    C4[n]=(1.0/(N-n))*C4[n]
 '''
N=len(u1)
ns=150
u1_bar = np.mean(u1)
u2_bar = np.mean(u2)
u3_bar = np.mean(u3)
u4_bar = np.mean(u4)

C1=np.zeros(ns)
C2=np.zeros(ns)
C3=np.zeros(ns)
C4=np.zeros(ns)

Tao1=np.zeros(ns)
Tao2=np.zeros(ns)
Tao3=np.zeros(ns)
Tao4=np.zeros(ns)

for n in range (0,ns):
    u1_plusn = u1[n:N]-u1_bar
    u1_minusn = u1[0:(N-n)]-u1_bar
    u2_plusn = u2[n:N]-u2_bar
    u2_minusn = u2[0:(N-n)]-u2_bar
    u3_plusn = u3[n:N]-u3_bar
    u3_minusn = u3[0:(N-n)]-u3_bar
    u4_plusn = u4[n:N]-u4_bar
    u4_minusn = u4[0:(N-n)]-u4_bar
                   
    C1[n] = (1.0/(N-n))*np.dot(u1_plusn,u1_minusn)
    C2[n] = (1.0/(N-n))*np.dot(u2_plusn,u2_minusn)
    C3[n] = (1.0/(N-n))*np.dot(u3_plusn,u3_minusn)
    C4[n] = (1.0/(N-n))*np.dot(u4_plusn,u4_minusn)
    
    Tao1[n]=1/2+(1/C1[0]*np.sum(C1[0:n]))
    Tao2[n]=1/2+(1/C2[0]*np.sum(C2[0:n]))
    Tao3[n]=1/2+(1/C3[0]*np.sum(C3[0:n]))
    Tao4[n]=1/2+(1/C4[0]*np.sum(C4[0:n]))
    
error1=math.sqrt(2*C1[0]/N*Tao1[ns-1])
error2=math.sqrt(2*C2[0]/N*Tao2[ns-1])
error3=math.sqrt(2*C3[0]/N*Tao3[ns-1])
error4=math.sqrt(2*C4[0]/N*Tao4[ns-1])


plt.figure(1)        
plt.plot(C1)
plt.ylabel('C1')
plt.savefig("C1.png")   

plt.figure(2)   
plt.plot(Tao1)
plt.ylabel('tao')
plt.savefig("Tao1.png")  

plt.figure(3)
plt.plot(C2)
plt.ylabel('C2')
plt.savefig("cor2.png")

plt.figure(4)
plt.plot(Tao2)
plt.ylabel('tao')
plt.savefig("Tao2.png") 

plt.figure(5)
plt.plot(C3)
plt.ylabel('C3')
plt.savefig("cor3.png")

plt.figure(6)
plt.plot(Tao3)
plt.ylabel('tao')
plt.savefig("Tao3.png") 

plt.figure(7)
plt.plot(C4)
plt.ylabel('C4')
plt.savefig("cor4.png")

plt.figure(8)
plt.plot(Tao4)
plt.ylabel('tao')
plt.savefig("Tao4.png")         

print(error1)
print(error2)
print(error3)
print(error4)

FILEdata1.close()  
FILEdata2.close()
FILEdata3.close()
FILEdata4.close()
'''FILEdata5.close() 
FILEdata6.close()'''