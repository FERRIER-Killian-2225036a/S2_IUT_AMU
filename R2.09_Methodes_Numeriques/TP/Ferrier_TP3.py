import matplotlib.pyplot as plt
import numpy as np

"""
Exercice 1:
"""
def puissance_dichotomique(x, n, compteur=0):
    if n == 1:
        return x, compteur
    elif n % 2 == 0:
        z, compteur = puissance_dichotomique(x, n/2, compteur)
        compteur += 1 
        return z*z, compteur
    else:
        z, compteur = puissance_dichotomique(x, (n-1)/2, compteur)
        compteur += 2 
        return x*z*z, compteur

x = 2
compteurMultiTableau = []
for n in range(1, 1001):
    result, compteurMulti = puissance_dichotomique(x, n)
    compteurMultiTableau.append(compteurMulti)

plt.plot(range(1, 1001), compteurMultiTableau, label="puissance_dichotomique")
plt.plot(range(1, 1001), np.floor(np.log2(range(1, 1001))), label="[log2(x)]")
plt.plot(range(1, 1001), 2 * np.floor(np.log2(range(1, 1001))), label="2[log2(x)]")
plt.xlabel("n")
plt.ylabel("Number of Multiplications")
plt.legend()
plt.show()

"""
Exercice 2:
"""
