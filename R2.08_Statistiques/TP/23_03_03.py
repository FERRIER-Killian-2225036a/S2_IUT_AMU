#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:45:02 2023

@author: killbib
"""
import numpy as np
import matplotlib.pyplot as plt

covid = np.array([
                (25.44, 9.64, 'Algeria'), (3367.85, 203.43, 'Argentina'), (80.87, 3.58, 'Australia'), 
                (290.67, 21.07, 'Austria'), (413.51, 24.52, 'Belgium'), (437.04, 64.16, 'Bulgaria'), 
                (678.71, 40.88, 'Canada'), (24.08, 1.42, 'Cyprus'), (594.11, 67.71, 'Czechia'),
                (41.75, 5.37, 'Denmark'), (31.67, 4.67, 'Estonia'), (29.51, 2.72, 'Finland'),
                (2689.36, 163.74, 'France'), (2764.98, 218.38, 'Germany'), (77.77, 10.1, 'Ireland'),
                (154.28, 13.66, 'Israel'), (1349.21, 176.33, 'Italy'), (14.35, 1.19, 'Luxembourg'),
                (722.32, 84.77, 'Malaysia'), (7.58, 0.72, 'Malta'), (433.79, 26.64, 'Netherlands'),
                (214.26, 33.48, 'Portugal'), (896.28, 118.56, 'Romania'), (147.79, 26.22, 'Serbia'), 
                (149.09, 39.98, 'Slovakia'), (115.18, 8.12, 'Slovenia'), (1692.84, 106.85, 'Spain'),
                (153.63, 18.84, 'Sweden'), (185.64, 12.4, 'Switzerland'), (1086.72, 210.26, 'United Kingdom'),
                (14074.58, 1312.24, 'United States')
                ])

Hosp = np.array(covid[:,0], dtype = np.float64)
Deces= np.array(covid[:,1], dtype = np.float64)
#%% Exo 1.1
print("Moyenne hospitalisation :", np.mean(Hosp,dtype = np.float64))
print("Moyenne deces :", np.mean(Deces,dtype = np.float64))

print("Quantile 1 hospitalisation :", np.quantile(Hosp,0.25))
print("Quantile 3 hospitalisation :", np.quantile(Hosp,0.75))

print("Quantile 1 deces :", np.quantile(Deces,0.25))
print("Quantile 3 deces :", np.quantile(Deces,0.75))

print("Mediane hospitalisation :", np.median(Hosp))
print("Mediane deces :", np.median(Deces))

print("Variance hospitalisation :", np.var(Hosp))
print("Variance deces :", np.var(Deces))

print("Ecart type hospitalisation :", np.std(Hosp))
print("Ecart type deces :", np.std(Deces))

#%% Exo 1.2
plt.scatter(Hosp, Deces)
plt.show()

#%% Exo 1.3
print("Covariance hospitalisation :", np.cov(Hosp, Deces)[0][1])
print("Coefficient de corrélation :", np.corrcoef(Hosp, Deces)[0][1])

#%% Exo 1.4


#%% Exo 1.5
a, b = np.polyfit(Hosp,Deces,1)
print("La droite de régression linéaire a pour équation y =",round(a,3),"x =",round(b,3))

#%% Exo 1.6
plt.scatter(Hosp, Deces)
x_trace = np.linspace(np.min(Hosp),np.max(Hosp))
plt.plot(x_trace, a*x_trace+b , 'red')
plt.show()

#%% Exo 2.1















































































































