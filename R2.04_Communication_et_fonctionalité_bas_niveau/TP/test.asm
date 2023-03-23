	.data
str: 	.asciiz "\nSomme = \n"
	.text
	ori $a2, $zero, 0
e1: 	ori $v0, $zero, 5 	#$v0 <- 5
	syscall
	or $a0, $zero, $v0 
	add $a2, $a2, $a0
	ori $v0, $zero, 1 	#$v0 <- 1
	syscall
	bne $a0, 0, e1 	#Si $a0!=100
	ori $v0, $zero, 4 
	la $a0, str
	syscall
	ori $v0, $zero, 10
	syscall