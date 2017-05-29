'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a*b*c.
'''
from math import sqrt

triples = [ ]
for a in range(1, 400):
	for b in range(1, 400):
		c = sqrt(a**2 + b**2)
		if c.is_integer():
			c = int(c)
			if a+b+c == 1000:
				print(a,b,c)
				print(a*b*c)
				quit()