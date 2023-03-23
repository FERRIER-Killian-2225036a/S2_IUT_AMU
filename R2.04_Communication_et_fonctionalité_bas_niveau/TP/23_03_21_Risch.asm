# Exercice 1 :
	.data
str: 	.asciiz "Ceci est une chaine de caracteres en ascii\n"
	.text
main:   ori $v0, $zero, 4 
	la $a0, str
	syscall 

# Exercice 2 :
	.text
	ori $t0, $zero, 2 	#$t0 <- 2
e1: 	ori $v0, $zero, 5 	#$v0 <- 5
	syscall
	or $a0, $zero, $v0 	#$a0 <- 5
	mul $a0, $a0, $t0 	#$a0 <- 5*2
	ori $v0, $zero, 1 	#$v0 <- 1
	syscall
	bne $a0, 100, e1 	#Si $a0!=100
	ori $v0, $zero, 10 	#$v0 <- 10
	syscall

	#1: Ce programme demande une saisie au clavier et fait la multiplication de 2 du chiffre donnée et recommence
	#   Le programme s'arrête quand le produit est égale a 100 donc avec une entrée = 50
	#2: C'est une boucle tant que
	#3: 
	.data
str: 	.asciiz "\nEntrez une valeur : \n"
	.text
	ori $t0, $zero, 2 	#$t0 <- 2
e1: 	ori $v0, $zero, 4 
	la $a0, str
	syscall			#Affiche la chaine de caractère
	ori $v0, $zero, 5 	#$v0 <- 5
	syscall
	or $a0, $zero, $v0 	#$a0 <- 5
	mul $a0, $a0, $t0 	#$a0 <- 5*2
	ori $v0, $zero, 1 	#$v0 <- 1
	syscall
	bne $a0, 100, e1 	#Si $a0!=100
	ori $v0, $zero, 10 	#$v0 <- 10
	syscall
	
	#4:
	.data
str: 	.asciiz "\nEntrez une valeur : \n"
	.text
	ori $t0, $zero, 2 	#$t0 <- 2
e1: 	ori $v0, $zero, 4 
	la $a0, str
	syscall			#Affiche la chaine de caractère
	ori $v0, $zero, 5 	#$v0 <- 5
	syscall
	or $a0, $zero, $v0 	#$a0 <- 5
	sll $a0, $a0, $t0 	#$a0 <- 5*2
	ori $v0, $zero, 1 	#$v0 <- 1
	syscall
	bne $a0, 100, e1 	#Si $a0!=100
	ori $v0, $zero, 10 	#$v0 <- 10
	syscall

# Exercice 3 :
