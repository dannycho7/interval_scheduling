import random
from math import pow

for x in range(int(pow(10, 3))):
	a = random.randint(1,100)
	b = random.randint(a+1,101)
	c = random.randint(1,101)
	print a, b, c
