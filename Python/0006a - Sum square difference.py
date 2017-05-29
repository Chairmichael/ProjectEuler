'''
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

sum_of_squares = 0
sum_squared = 0
the_sum = 0
for x in range(1,101):
	sum_of_squares = sum_of_squares + x**2
	the_sum = the_sum + x
sum_squared = the_sum**2
print(sum_squared-sum_of_squares)