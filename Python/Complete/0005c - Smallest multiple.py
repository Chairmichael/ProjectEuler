'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
# ~7.6seconds

divisors = [20, 19, 18, 17, 16, 15, 14, 13, 11]
for num in range(20, int(1e10), 20):
	found = True
	for div in divisors:
		if num % div != 0:
			found = False
			break
	if found:
		print(num)
		break