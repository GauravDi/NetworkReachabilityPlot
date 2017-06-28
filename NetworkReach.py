#author : Gaurav Diwate. gadi5945@colorado.edu
#name   : file2.py
#purpose: Program to create a LINE GRAPH for ping times.
#Date   : 2015.07.11
#version: 1.0.0

import subprocess
import re
import matplotlib.pyplot as plt
import sys
from prettytable import PrettyTable

print("pinging 8.8.8.X....")
print()
h=0

try:
    Q=[line.rpartition('_')[-1] for line in subprocess.check_output("ping -n 50 8.8.8.8").splitlines()[2:-4]]
except:
    Q="Request timed out."
    
i=0
j=0
g=0
k=0
w=0
k=0
x=[]
while i<50:
    if Q!="Request timed out.":
        while w<50:
            comp=re.search(r'time=\d{1,4}',Q[i])
            if hasattr(comp,'group'):
                T=comp.group(0)[5:9]
                x.append(T)
                w=w+1
                i=i+1
            else:
                T=0
                x.append(T)
                w=w+1
                i=i+1
                k=k+1
                if k==5:
                    plt.plot(x,marker='o')
                    break
        plt.plot(x,marker='o')
    else:
        T=0
        x.append(T)
        i=i+1 
        g=g+1
        if g==5:
            plt.plot(x,marker='o')
            s=1
            while s<46:
                x.append('-')
                s=s+1
                i=i+1
                g=g+1
                        
print("pings for 8.8.8.X are done")
print()
print("pinging 4.2.2.X....")

try:
    A=[line.rpartition('_')[-1] for line in subprocess.check_output("ping -n 50 4.2.2.1").splitlines()[2:-4]]
except:
    A="Request timed out."
n=0
d=0
e=0
l=0
y=[]
while n<50:
    if A!="Request timed out.":
        while d<50: 
            comp=re.search(r'time=\d{1,4}',A[n])
            if hasattr(comp,'group'):
                B=comp.group(0)[5:9]
                y.append(B)
                n=n+1
                d=d+1
            else:
                B=0
                y.append(B)
                n=n+1
                d=d+1
                l=l+1
                if l==5:
                    plt.plot(y,marker='o')
                    break
        plt.plot(y,marker='o')
    else:
        B=0
        y.append(B)
        n=n+1
        e=e+1
        if e==5:
            plt.plot(y,marker='o')
            t=1
            while t<46:
                y.append('-')
                t=t+1    
                n=n+1
                e=e+1                
       
print()
print("pings for 4.2.2.X are done")  
print()
print("Table For Ping Timings:")        
u=0
table=PrettyTable(["TIME FOR 8.8.8.8","TIME FOR 4.2.2.1"])
while u<50:
    table.add_row([x[u],y[u]])
    u=u+1
print(table)

plt.ylabel("TIME IN ms")
plt.xlabel("NUMBER OF PINGS")
plt.title("LINE GRPAH")
plt.margins(0.025)
plt.legend(['ping for 8.8.8.8', 'ping for 4.2.2.1'], loc='upper left')
if len(sys.argv)==2:
    try:
        j=sys.argv[1].split('.')
        if j[1]==".gif":
            print()
            print("FILE NOT SAVED: INCORRECT FILE FORMAT:FORMAT SHOULD BE (name.png/name.jpg)")
            plt.show()
        else:
            plt.savefig(sys.argv[1])
            plt.show()
    except:
        print()
        print("ERROR:FILE IS NOT SAVED:EXTENSION IS REQUIRED(.png/.jpg)")
        plt.show()
else:
    plt.show()