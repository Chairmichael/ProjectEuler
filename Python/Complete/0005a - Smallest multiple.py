'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
# ~13.4seconds
# from time import perf_counter
# start = perf_counter()

for num in range(20, int(1e10), 20):
	found = True
	for div in range(2,21):
		if num % div != 0:
			found = False
			break
	if found:
		print(num)
		break

# end = perf_counter()
# print('Elapsed seconds: {}'.format(end-start))