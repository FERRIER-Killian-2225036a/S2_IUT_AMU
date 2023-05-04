#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:47:29 2023

@author: killbib
"""

import numpy as np
from numpy.linalg import matrix_power

#Exo1:
M = np.array([[0,0,0,0,1,1,1,0,0,1],#0
              [0,0,0,0,1,0,0,0,0,1],#1
              [0,0,0,0,1,0,0,1,0,0],#2
              [0,0,0,0,0,1,0,0,0,0],#3
              [1,1,1,0,0,0,0,1,0,1],#4
              [1,0,0,1,0,0,0,1,1,0],#5
              [1,0,0,0,0,0,0,1,0,0],#6
              [0,0,1,0,1,1,1,0,1,0],#7
              [0,0,0,0,0,1,0,1,0,0],#8
              [1,1,0,0,1,0,0,0,0,0],#9
              ])
#%% Exo2:
print("M² =",matrix_power(M,2)[6][2])

#%% Exo3:
result = 0
for i in range(1,6):
    result += matrix_power(M,i)[6][2]
print("Nombre de chemin de 2 à 6 de longeure >= 5 :",result)

#%% Exo4:
def distance (M,X,Y):
    i = 1
    while M[X][Y]==0:
        M = matrix_power(M,i+1)
        i+=1
    return i
print("La distance entre 1 et 5 est :",distance(M, 1, 5))

#%% Exo5:
