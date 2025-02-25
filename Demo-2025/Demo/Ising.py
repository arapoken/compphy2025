
# IsingVP.py: Ising model, with VPython

"""Dirichlet boundary conditions surrounding four walls 
 Domain dimensions: WxH, with 2 triangles per square  
 Based on FEM2DL_Box Matlab program in Polycarpou, Intro Finite 
 Element Method in Electromagnetics, Morgan & Claypool (2006) """

from vpython import *
import random
import numpy as np

import time
time.sleep(10)


scene = canvas(x=0,y=0,width=1400,height=300, range=10)
engraph = graph(y=200,width=1400,height=300, 
        title='1D Ising Model: Energy of Spin System', xtitle='iteration', 
        ytitle='E',xmax=500, xmin=0, ymax=5, ymin=-5)
enplot = gcurve(color=color.blue, graph=engraph)                  
N = 30; B = 1.;  mu = .33;  J = .20;  k = 1.;  T  = 100.                                                 
state = np.zeros((N));   S = np. zeros((N) ,float)                   
test  = state                                               
random.seed()                            

def energy (S) :                                  
    FirstTerm = 0.
    SecondTerm = 0.                                          
    for  i in range(0,N-2):  FirstTerm += S[i]*S[i + 1]
    FirstTerm *= -J 
    for i in range(0,N-1):   SecondTerm += S[i]
    SecondTerm *= -B*mu; 
    return (FirstTerm + SecondTerm); 

ES = energy(state)                                   

def spstate(state):                           # Plots spins  
    for obj in scene.objects: obj.visible = 0 # Erase arrows
    j = 0    
    for i in range(-N,N,2):               
        if state[j]==-1:  ypos = 5             # Spin down
        else:             ypos = 0
        if 5*state[j]<0: 
            arrowcol = vector(1,1,1)  # White = down
        else:             
            arrowcol = vector(0.7,0.8,0)
        arrow(pos=vector(i,ypos,0),axis=vector(0,5*state[j],0),color=arrowcol) 
        j += 1

for  i in range(0 ,N):  state[i] = -1  # Initial spins all down

for obj in scene.objects:   obj.visible = 0
spstate(state)                       
ES = energy(state)                   

for  j in range (1,500):             
    rate(30)                        
    test = state      
    #print('ko')             
    r = int(N*random.random());   # Flip spin randomly
    test[r] *= -1                  
    ET = energy(test)              
    p = np.exp((ES-ET)/(k*T))   #  Boltzmann test
    enplot.plot(pos=(j,ES))       # Adds segment to curve
    if p >= random.random():       
        state = test
        spstate(state)
        ES = ET
