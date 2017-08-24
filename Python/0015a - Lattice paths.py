'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

sidelength = 20
paths = [ ]
lefts = 0
rights = 0
done = False
while not done:
	for x in range(2*sidelength):
		pass