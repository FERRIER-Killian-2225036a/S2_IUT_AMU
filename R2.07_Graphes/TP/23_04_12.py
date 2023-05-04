#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 10:31:00 2023

@author: killbib
"""

import networkx as nx
import matplotlib.pyplot as plt

# On crée un graphe vide
G= nx.Graph()

# On ajoute les sommets 
G.add_nodes_from([0,1,2,3,4,5,6,7,8])  # une liste de sommets

G.add_edges_from([(1,9),(1,4)])   # une liste d'arêtes
G.add_edges_from([(4,2),(4,0),(4,7),(4,9)])
G.add_edges_from([(0,9),(0,6),(0,5)])
G.add_edges_from([(6,7)])
G.add_edges_from([(1,9),(1,4)])
G.add_edges_from([(5,3),(5,8),(5,7)])
G.add_edges_from([(8,7),(7,2)])
                 
# Si on ajoute une arete avec un sommet inconnu celui-ci sera automatiquement créé
G.add_edge(1,4)

nx.draw(G, with_labels=True)  # Tracé du graphe
plt.show()