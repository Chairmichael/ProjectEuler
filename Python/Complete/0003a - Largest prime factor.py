'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from math import sqrt

subject = 600851475143

for x in range(int(sqrt(subject))+1, 3, -2):
	if subject % x == 0:
		is_prime = True
		for y in range(3, int(x/2)+1, 2):
			if x % y == 0:
				is_prime = False
				break
		if is_prime:
			print(x)
			break