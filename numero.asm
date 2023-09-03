L1: add $s1, $s2, $s3
L2:	sub $s1, $s2, $s3
	addi $s1, $s2, 100
	addu $s1, $s2, $s3
	subu $s1, $s2, $s3
	addiu $s1, $s2, 100
	mul $s1, $s2, $s3
	mult $s2, $s3
	multu $s2, $s3
	div $s2, $s3
	and $s1, $s2, $s3
	or $s1, $s2, $s3
	andi $s1, $s2, 100
	ori $s1, $s2, 100
	sll $s1, $s2, 10
	srl $s1, $s2, 10
	lw $s1, 100($s2)
	sw $s1, 100($s2)
	lui $s1, 100
	mfhi $s2
	mflo $s2
L3:	beq $s1, $s2, L1
 	bne $s1, $s2, L2
	slt $s1, $s2, $s3
	slti $s1, $s2, 100
	j L1
	jr $s1
	jal L3