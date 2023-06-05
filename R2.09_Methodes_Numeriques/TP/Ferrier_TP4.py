### Exo 1.1
def Dichotomie(f, a, b, e):
    iterations = 0
    while abs(b - a) > e:
        c = (a + b) / 2
        if f(c) == 0:
            return c, iterations
        elif f(a) * f(c) <= 0:
            b = c
        else:
            a = c
        iterations += 1

    return (a + b) / 2, iterations


### Exo 1.2
def f1(x):
    return x * x

a = -2
b = 1
e = 0.001

centreDernierIntervalle, iterations = Dichotomie(f1, a, b, e)
print("f(x) s'annule en x =", centreDernierIntervalle, " après ", iterations, " itérations.")


### Exo 1.3
def f2(x):
    return x - 1

centreDernierIntervalle, iterations = Dichotomie(f2, a, b, e)
print("f(x) s'annule en x =", centreDernierIntervalle, " après ", iterations, " itérations.")


### Exo 1.4
import math

### a)
def f3(x, c):
    return math.pow(x, 1 / (2 - c))

### b)
c = 36
if c > 1:
    print("Les conditions f(0) < 0 et f(c + 1) > 0 ne peuvent pas être vérifiées pour c > 1.")
else:
    if f3(0, c) < 0 and f3(c + 1, c) > 0:
        print("Les conditions f(0) < 0 et f(c + 1) > 0 sont vérifiées pour c =", c)

### c)
def RacineDichotomie(c, e):
    def f(x):
        return math.pow(x, 1 / (2 - c)) if c < 1 else 0
    return Dichotomie(f, 0, c + 1, e)

### d)
c = 36
e = 1e-15
if c > 1:
    print("La fonction Racine Dichotomie ne peut pas être utilisée pour c > 1.")
else:
    centreDernierIntervalle, iterations = RacineDichotomie(c, e)
    print("Une approximation de la racine carrée de ", c, " est ", centreDernierIntervalle, " après ", iterations, " itérations.")


### Exo 2.1
def f(x):
	return (1/2)*(x+(c/x))