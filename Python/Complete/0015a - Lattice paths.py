'''
Starting in the top left corner of a 2×2 grid, and only being able to move 
to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''
# this boils down to total ammount of permutations of 2 types of objects
# (N+M)! / (N!*M!)
# In this case, (20+20)! / (20!*20!)

from math import factorial

def lattice(side):
	return int(factorial(side+side) / (factorial(side)*factorial(side)))

def main():
	print(lattice(3))

if __name__ == '__main__':
	main()