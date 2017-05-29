'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
# ~18.5seconds

for num in range(20, int(1e10), 20):
	if all(num%div == 0 for div in range(2,21)):
		print(num)
		break
