'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
'''
from math import sqrt

primes = [ ]
num = 3
found = False
while not found:
	is_prime = True
	for div in range(3, int(sqrt(num))+1):
		if num % div == 0:
			is_prime = False
			break
	if is_prime:
		primes.append(num)
	if len(primes) == 10000:
		print(primes[-1])
		break
	num = num + 2

print(len(primes))