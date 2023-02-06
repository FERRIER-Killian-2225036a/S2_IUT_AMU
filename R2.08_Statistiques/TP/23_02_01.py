#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 14:07:08 2023

@author: Killian Ferrier
"""
import numpy as np

def printTabl(tab):
    for i in range(len(tab)):
        print(tab[i])

serieStat = np.array([14.5,17,8,6,9,12,11,15,8,11,7.5,14.5,6,17,7.5,9,15,14,12,9])
serieStat.sort()

serieStatUnique = np.unique(serieStat, return_counts=True)

modalite = serieStatUnique[0]

"""
def effectif(serieStat,modalite):
    effectif = np.ones((len(modalite),), dtype=int)
    placeDansTableau=0
    for i in range(len(serieStat)-1):
        if serieStat[i]==serieStat[i+1]:
            effectif[placeDansTableau]+=1
        else :
            placeDansTableau+=1
    return effectif
"""
effectif = serieStatUnique[1]

"""
def frequence(effectif,serieStat):
    arrayFrequence = np.zeros(len(effectif),)
    for i in range(len(effectif)):
        arrayFrequence[i] = effectif[i]/len(serieStat)
    printTabl(arrayFrequence)
"""
frequence = np.array(effectif/len(serieStat))

effectifCumule = np.cumsum(effectif)

frequenceCumule = np.cumsum(frequence)


def calculMode(effectif,modalite):
    maxi = 0
    for i in range(len(effectif)): 
        if (effectif[i]>maxi): 
            maxi = effectif[i]
    return modalite[maxi]

maxi = np.index_exp(np.max(modalite)) 

#mode = calculMode(effectif, modalite)
print(maxi)










































































