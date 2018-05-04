#/usr/bin/env
# 0025a - 1000-digit Fibonacci number.py

'''
The Fibonacci sequence is defined by the recurrence relation:
Hence the first 12 terms will be:
The 12th term, F
, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000
digits?
'''

def fib(i):
    a, b = 0, 1
    if i != 0:    
        for x in range(0, i):
            yield b
            a, b = b, a + b
    else:
        while True:
            yield b
            a, b = b, a + b
def main():
    for i, n in enumerate(fib(0)):
        if len(str(n)) == 1000:
            print(n)
            print(f'Found at index: {i}')
            break


if __name__ == '__main__':
    import os, sys
    main()
