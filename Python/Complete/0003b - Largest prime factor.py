#/usr/bin/env 
# 0003b - Largest prime factor.py

'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or not n % 2: return False
    if n < 9: return True
    if not n % 3: return False
    root = int(n**0.5)
    div = 5
    while div <= root:
        if not n % div: return False
        if not n % (div+2): return False
        div += 6
    return True

# Generates the prime factors
def prime_factors(n, direction='down'):
    # Get n's square root
    n_root = int(n**0.5)
    # Make n's root odd
    if not n_root % 2: n_root += 1
    print(n_root)
    if direction.lower() == 'down':
        for div in range(n_root, 3, -2):
            if not n % div and is_prime(n): yield div
    if direction.lower() == 'up':
        for div in range(3, n_root, 2):
            if not n % div and is_prime(n): yield div

def main():
    [print(x) for x in prime_factors(13195)]

if __name__ == '__main__':
    import os, sys
    main()
