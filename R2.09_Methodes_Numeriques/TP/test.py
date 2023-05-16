import matplotlib.pyplot as plt
import numpy as np

def puissance_dichotomique(x, n, count=0):
    if n == 1:
        return x, count
    elif n % 2 == 0:
        z, count = puissance_dichotomique(x, n/2, count)
        count += 1  # Increment count for the multiplication z*z
        return z*z, count
    else:
        z, count = puissance_dichotomique(x, (n-1)/2, count)
        count += 2  # Increment count for the multiplications x*z*z
        return x*z*z, count

x = 2
multiplication_counts = []
for n in range(1, 1001):
    result, multiplication_count = puissance_dichotomique(x, n)
    multiplication_counts.append(multiplication_count)

# Plotting the number of multiplications as a function of n
plt.plot(range(1, 1001), multiplication_counts, label="puissance_dichotomique")
plt.plot(range(1, 1001), np.floor(np.log2(range(1, 1001))), label="[log2(x)]")
plt.plot(range(1, 1001), 2 * np.floor(np.log2(range(1, 1001))), label="2[log2(x)]")
plt.xlabel("n")
plt.ylabel("Number of Multiplications")
plt.legend()
plt.show()