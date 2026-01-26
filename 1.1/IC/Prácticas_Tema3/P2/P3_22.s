.data
cadena: .asciiz "Hola mundo"


.text
.globl main

main:
	la $a0, cadena	# guardamos en $a0 al dirección de la cadena
	addi $v0, $0, 4	# Impresión de la cadena en pantalla
	salto:
		syscall    # llamada al sistema
	j salto

	addi $v0, $0, 10
	syscall
