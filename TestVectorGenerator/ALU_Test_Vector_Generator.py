import random

file=open('../TestVector/ALU_Test_Vector.txt', 'w')
file.write('A[32] B[32] Op[4] Sa[5] C[32] V')

for i in range (50000):
	r1 = random.randint(-2**31, 2**31-1)
	r2 = random.randint(-2**31, 2**31-1)
	Op = random.randint(0,15)
	Sa = random.randint(0,31)
	V = 0
	if (Op == 0 or Op == 1): #Shift Left Logical
		C = r2 << Sa
		if C > 2**31 or C < -2**31:
			C = int(((C/2**32) % 1) * 2**32)
	elif (Op == 2 or Op == 3): #Add
		C = r1 + r2
		if C >= 2**31:
			C = C - 2**32
			V = 1
		if C < -2**31:
			C = C + 2**32
			V = 1
	elif (Op == 4): #And
		C= r1 & r2
	elif (Op == 5): #Or
		C= r1 | r2
	elif (Op == 6 or Op == 7): #Subtract
		C = r1 - r2
		if C >= 2**31:
			C = C - 2**32
			V = 1			
		if C < -2**31:
			V = 1
			C = C + 2**32
	elif (Op == 8): #Not Equal
		if(r1 != r2):
			C = 1
		else:
			C = 0
	elif (Op == 9): #Equal
		if (r1 == r2):
			C = 1
		else:
			C = 0
	elif (Op == 10): #Xor
		C = r1^r2
	elif (Op == 11): #Nor
		C = ~(r1 | r2)
	elif (Op == 12): #Shift Right Logical
		if r2 < 0:
			r2 = r2 + 2**32
		C = r2 >> Sa				
	elif (Op == 13): #Shift Right Arithmetic
		C = r2 >> Sa
		if C > 2**31 or C < -2**31:
			C = int(((C/2**32) % 1) * 2**32)
	elif (Op == 14): #Less Than or Equal to Zero	
		if (r1 <= 0):
			C = 1
		else:
			C = 0
	elif (Op == 15): #Greater than Zero
		if(r1 > 0):
			C = 1
		else:
			C = 0
	file.write('\n%s\t%s\t%s\t%s\t%s\t%s' %(r1, r2, Op, Sa, C, V))		
