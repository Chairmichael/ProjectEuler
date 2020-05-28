# 0051a - Prime digit replacements.py
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

import itertools

# prime_amount: Target amount of primes for the value family
# max_replace_digits: Replace up to this many digits
def find_smallest_replace_prime(ceiling, prime_amount, max_replace_digits):
    for x in range(11, ceiling, 2):
        for i in range(3,max_replace_digits): 
            for n in get_replacements(x, i+1):
                primes_found = 0
                the_number = ''
                if the_number == '':
                    the_number = n
                for j in range(10):
                    z = int(n.replace('*', str(j)))
                    if is_prime(z):
                        primes_found+=1
                if primes_found == prime_amount:
                    print(f'\t### {the_number} ### \t\t primes: {primes_found}')
    

#   s: number to get replacement numbers from;
#   n: amount of replacement digits to use
def get_replacements(s, n):
    s = str(s)
    end_digit = s[-1]
    base_num = s[0:-1]
    numbers_used = [ ]
    for x in itertools.permutations(base_num + '*'*n):
        # for i in range(0,10):
        #     y = ''.join(x + tuple(end_digit))
        #     z = str(y).replace('*', str(i))
        #     if not z in numbers_used:
        #         numbers_used.append(z)
        #         yield z
        z = ''.join(x + tuple(end_digit))
        if not z in numbers_used:
            numbers_used.append(z)
            yield z

def factors(x):
    i = 1
    # This will loop from 1 to int(sqrt(x))
    while i*i <= x:
        if x % i == 0:
            yield i
            if x//i != i:
                yield x//i
        i += 1

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
    find_smallest_replace_prime(
        ceiling=10000, prime_amount=8, max_replace_digits=4)
    # 56003


if __name__ == '__main__':
    main()
