from math import sqrt

X = [2,8,6,9,3,4,4,5,10,9,9,8,7,6]

#Exercice 1.1
def Moyenne(X):
	return sum(X)/len(X)
#Exercice 1.2
def EcartType(X):
	moyenne=Moyenne(X)
	Variance=0
	for i in range(len(x)):
		Variance=((X[i])-moyenne)**2
	Variance=Variance/len(X)
	EcartType=sqrt(Variance)
	print(EcartType)
#Exercice 2.1
def Mediane(X):
	X.sort()
	if(len(X)%2==1):
		print(X[len(X)//2])
	else:
		print((X[len(X)//2]+X[len(X)//2+1])/2)
#Exercice 2.2
def MedianeSousPartie(X):
	X.sort()
	if(len(X)%2==1):
		return X[len(X)//2], X[:len(X)//2],X[len(X)//2+1:]
	else:
		return(X[len(X)//2]+X[len(X)//2+1])/2, X[:len(X)//2],X[len(X)//2:]
MedianeSousPartie(X)
#Exercice 2.3
def Quartile(X):
	Rsmediane = Mediane(X)
	med=Rsmediane[0]
	gauche=Rsmediane[1]
	droite=Rsmediane[2]
	Quartile1=Mediane(gauche)
	Quartile3=Mediane(droite)
	return Quartile1,med,Quartile3
#Exercice 3.1
def Maximun(X):
	return max(X)
#Exercice 3.2
def Iteration(X):
	Tableau1=[]
	for i in range(len(X)):
