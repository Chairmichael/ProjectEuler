# 0024a - Prime digit replacements.py
# Jefferson V. Henry
'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime
with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
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

def main():
    pass

if __name__ == '__main__':
    main()
