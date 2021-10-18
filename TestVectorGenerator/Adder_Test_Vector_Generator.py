import random

file=open('../TestVector/Adder_Test_Vector.txt', 'w')
file.write('A[32] B[32] Cin C[32] V')

for i in range (10000):
	r1 = random.randint(-2**31, 2**31-1)
	r2 = random.randint(-2**31, 2**31-1)
	Cin = random.randint(0,1)
	C= r1+r2+Cin
	V = 0
	if C >= 2**31:
		C=C-2**32
		V=1
	if C < -2**31:
		C=C+2**32
		V=1
	file.write('\n%s\t%s\t%s\t%s\t%s' %(r1, r2, Cin, C, V))
