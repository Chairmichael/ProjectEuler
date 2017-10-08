#!/usr/bin/env 
# 0023a - Non-abundant sums.py

'''
A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is 
less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. However, this upper limit 
cannot be reduced any further by analysis even though it is known that the 
greatest number that cannot be expressed as the sum of two abundant numbers 
is less than this limit.

Find the sum of all the positive integers which 
cannot be written as the sum of two abundant numbers.
'''


def divisors(n):
	# return [d for d in range(1, (n//2)+1) if n % d == 0]
	for d in range(1, (n//2)+1):
		if n % d == 0: yield d

def adundant_nums(ceiling):
	# dbg = print('n\t\ts\t\tdivisors')
	for n in range(12, ceiling+1):
		s = sum(divisors(n))
		if s > n:
			if 'dbg' in locals():
				print(f'{n}\t\t{s}\t\t{[x for x in divisors(n)]}')
			yield n


def main():
	print('getting abundant numbers')
	list_abund = [x for x in adundant_nums(28123)]
	print('getting special numbers')
	spec_nums = [ ]
	for n in range(28123):
		for x in list_abund:
			if x > n: spec_nums.append(n)
			for y in list_abund:
				if y > n: spec_nums.append(n)
				if x + y == n: break


	print(sum(list(set(spec_nums))))

if __name__ == '__main__':
	main()
