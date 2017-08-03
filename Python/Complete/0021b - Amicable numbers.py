'''
Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair 
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
from math import sqrt
def divisors_sum(n):
	return sum([d for d in range(1, int(n//2)+1) if n%d==0])
print(sum([n for n in range(1, 10000) if n==divisors_sum(divisors_sum(n)) and n!=divisors_sum(n)]))