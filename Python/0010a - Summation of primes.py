'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from math import sqrt

prime_sum = 2
for num in range(3, int(2e6), 2):
	is_prime = True
	for div in range(3, int(sqrt(num))+1):
		if num % div == 0:
			is_prime = False
			break
	if is_prime:
		prime_sum = prime_sum + num
print(prime_sum)