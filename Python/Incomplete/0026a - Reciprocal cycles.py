#/usr/bin/env 
# 0026a - Reciprocal cycles.py

'''
A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:
    1/2 =   0.5
    1/3 =   0.(3)
    1/4 =   0.25
    1/5 =   0.2
    1/6 =   0.1(6)
    1/7 =   0.(142857)
    1/8 =   0.125
    1/9 =   0.(1)
    1/10    =   0.1 
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
its decimal fraction part.
'''

import decimal
D = decimal.Decimal
LENGTH = 1000

# TODO: Fix for fractions that start cycling after the first decimal place
def principal_period(s):
    print(s)
    if len(s) != LENGTH:
        return 0
    for i in range(1, len(s)):
        sub = s[:i]
        x = len(s) // len(sub)
        if sub*x == s[:len(sub)*x]:
            print(len(sub))
            return len(sub)
    else:
        return -1

# generates reciprocals of the natural numbers up to a ceiling
def nat_rcp(ceiling):
    one = D(1)
    for n in range(1, ceiling):
        yield n, one / D(n)

def main():
    largest = 0
    decimal.getcontext().prec = LENGTH
    decimal.getcontext().rounding = decimal.ROUND_FLOOR
    principal_period(str(D(1)/D(7))[2:])
    # for n, x in nat_rcp(1000):
    #     p = principal_period(str(x)[2:])
        # if p != 0:
        #     if p > largest:
        #         largest = p
        #         print(n, p)
        #     else:
        #         print(n, p)
        # elif p == -1:
        #     print(f'\t## {n}')
        #     input()

if __name__ == '__main__':
    main()
