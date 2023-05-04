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
str:	.asciiz "\nEntrez une valeur : \n"
    	.text
    	ori $t0, $zero, 2     #$t0 <- 2
e1: 	ori $v0, $zero, 4 
    	la $a0, str
    	syscall            #Affiche la chaine de caractère
    	ori $v0, $zero, 5     #$v0 <- 5
    	syscall
    	or $a0, $zero, $v0     #$a0 <- 5
    	sll $a0, $a0,1     #$a0 <- 5*2 au lieu de mul $a0,$a0,$t0
    	ori $v0, $zero, 1     #$v0 <- 1
    	syscall
    	bne $a0, 100, e1     #Si $a0!=100
    	ori $v0, $zero, 10     #$v0 <- 10
    	syscall

# Exercice 3 :
	.data
input_msg: .asciiz "Entrez un entier (0 pour arrêter) : "
sum_msg: .asciiz "Somme = "
newline: .asciiz "\n"
	.text
main:   addi $s0, $zero, 0      # initialiser la somme à zéro
        addi $v0, $zero, 4      # numéro de l'appel système pour afficher une chaîne de caractères
        la $a0, input_msg       # charger l'adresse de la chaîne de caractères à afficher
        syscall
loop:   addi $v0, $zero, 5      # numéro de l'appel système pour lire un entier depuis l'entrée standard (clavier)
        syscall
        add $s0, $s0, $v0       # ajouter l'entier lu à la somme totale
        beq $v0, $zero, exit    # sortir de la boucle si l'entrée est zéro
        j loop                  # répéter la boucle
exit:   addi $v0, $zero, 4      # numéro de l'appel système pour afficher une chaîne de caractères
        la $a0, sum_msg         # charger l'adresse de la chaîne de caractères à afficher
        syscall
        addi $v0, $zero, 1      # numéro de l'appel système pour afficher un entier
        move $a0, $s0           # charger la somme totale à afficher
        syscall
        addi $v0, $zero, 4      # numéro de l'appel système pour afficher une chaîne de caractères
        la $a0, newline         # charger l'adresse du caractère de nouvelle ligne à afficher
        syscall
        addi $v0, $zero, 10     # numéro de l'appel système pour sortir du programme
        syscall

# Exercice 4 :
