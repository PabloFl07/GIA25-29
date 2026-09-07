.data

.text
.globl main


main:

      addi $t0, $0, 5
      addi $t1, $0, -33  #  [0x00400004] /  00100000000010011111111111011111
      add  $t2, $t0, $t1 # [0x00400008] / 00000001000010010101000000100000

      addi $t3 , $0 , -512
      addi $t4 , $0 , 1024
      add $t5 , $t3 , $t4
	
      addi $v0, $0, 10 # Indica el codigo de syscall ( 10 es para cerrar )	
      syscall