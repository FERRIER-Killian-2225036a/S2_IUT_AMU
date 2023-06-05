def lagrange_elementaire(X, i, x):
    result = 1
    for j in range(len(X)):
        if j == i:
            continue
        result *= (x - X[j]) / (X[i] - X[j])
    return result

def test_lagrange_elementaire():
    X = [1, 2, 3]
    print(lagrange_elementaire(X, 0, 1))  # Output: 1
    print(lagrange_elementaire(X, 0, 2))  # Output: 0
    print(lagrange_elementaire(X, 0, 3))   # Output: 0

def lagrange(X, Y, x):
    result = 0
    for i in range(len(X)):
        result += Y[i] * lagrange_elementaire(X, i, x)
    return result

def test_lagrange():
    X = [1, 2, 3]
    Y = [1, 4, 9]
    print(lagrange(X, Y, 1))  # Output: 1
    print(lagrange(X, Y, 2))  # Output: 4
    print(lagrange(X, Y, 3))  # Output: 9

test_lagrange_elementaire()
test_lagrange()


import numpy as np
import matplotlib.pyplot as plt

X = [1, 2, 3]
Y = [1, 4, 9]

# Tracer les points de données
plt.scatter(X, Y, color='red', label='Données')

# Tracer le polynôme d'interpolation
x_vals = np.linspace(min(X), max(X), 100)
y_vals = [lagrange(X, Y, x) for x in x_vals]
plt.plot(x_vals, y_vals, color='blue', label='Interpolation')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()