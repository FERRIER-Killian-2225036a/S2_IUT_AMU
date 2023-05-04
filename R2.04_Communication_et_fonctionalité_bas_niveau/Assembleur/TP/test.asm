	.data
str: 	.asciiz "T : \n"
espace: .word "   "
	
tableau:.word 	0x00000001,
		0x00000002,
		0x00000003,
		0x00000004,
		0x00000005
	.text
main: 	la $t1, tableau
	ori $v0, $zero, 4      # numéro de l'appel système pour afficher une chaîne de caractères
        la $a1, str       # charger l'adresse de la chaîne de caractères à afficher
        syscall
for:	sll $t1, $s3, 2 # t1 <- 4*i
	add $t1, $t1, $s6 # t1 <- adresse de save[i]
	lw $t0, 0($t1) # t0 <- save[i]
	bne $t0, $s5, exit # goto Exit if save[i]!=k
	addi $s3, $s3, 1 # i += 1
	j for
    	li $v0, 4
    	syscall
exit:	