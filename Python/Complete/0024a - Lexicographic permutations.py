# 0024a - Lexicographic permutatons.py
# Jefferson V. Henry
'''
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

from itertools import *

def main():
    p = permutations(range(10))
    i = 1
    for x in p:
        if i == 1000000:
            print(''.join(str(n) for n in x))
            break
        i += 1

if __name__ == '__main__':
    main()
