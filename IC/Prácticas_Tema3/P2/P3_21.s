.data

cadena: .asciiz "hola mundo"
.text
.globl main
main:
	addi $t0 , $0 , 3        # Contador = 3
	la $a0, cadena          # Carga la direccion de caneda
	addi $v0, $0, 4          # Codigo para imprimir por pantalla

	salto:
		syscall
		addi $t0,$t0, -1
	bne $t0 ,$0 ,salto      # Si $t0 != 0 , salta

	addi $v0, $0, 10
	syscall