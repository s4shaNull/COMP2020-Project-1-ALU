import random

file=open('../TestVector/Left_Shifter_Test_Vector.txt', 'w')
file.write('B[32] Sa[5] C[32]')

for i in range (10000):
	r2 = random.randint(-2**31, 2**31-1)
	Sa = random.randint(0,31)
	C = r2 << Sa
	if C > 2**31 or C < -2**31:
		C = int(((C/2**32) % 1) * 2**32)
	file.write('\n%s\t%s\t%s'%(r2, Sa, C))

	
	
	
