# 0023a - Non-abundant sums.py
#   Jefferson V. Henry

'''
A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is 
less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. However, this upper limit 
cannot be reduced any further by analysis even though it is known that the 
greatest number that cannot be expressed as the sum of two abundant numbers 
is less than this limit.

Find the sum of all the positive integers which
cannot be written as the sum of two abundant numbers.
'''


# def is_sum_two_abundants(n, nums):
#     for x in nums:
#         for y in nums:
#             if n == x+y:
#                 return [x,y]
#     return []

from bisect import bisect_left
def take_closest(myList, myNumber):
    # Assumes myList is sorted. Returns closest value to myNumber.
    # If two numbers are equally close, return the largest number.
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
       return after 
    else:
       return before


def is_sum_two_abundants(n, nums):
    i = 0
    j = nums.index(take_closest(nums, n)) + 1
    i_increment = True
    while i < j:
        try:
            if nums[i] + nums[j] == n:
                return True
            # change searching indexes
            elif i_increment: 
                i += 1
                i_increment = False
            else: 
                j -= 1
                i_increment = True
        except:
            print(f'i = {i}  j = {j}  n = {n}')
            raise
    return False

def is_abundant_num(n):
    # sum proper divisors
    n_sum = 1
    ceiling = int((n/2) + 1) # need to add one, bc range() end is exclusive
    for div in range(2, ceiling):
        if n % div == 0:
            n_sum += div
    return n_sum > n

def get_adundant_nums(ceiling):
    for x in range(1, ceiling):
        if is_abundant_num(x):
            yield x

def main():
    # [print(x) for x in get_adundant_nums(28123)]
    print('getting list')
    nums = [x for x in get_adundant_nums(30000)]
    print(f'len(nums) = {len(nums)}')
    print('calculating sum')
    # Get numbers that are the sum of two abundant numbers
    the_sum = 0
    for x in range(28123+1):
        if not is_sum_two_abundants(x, nums):
            the_sum += x
    print(the_sum)


if __name__ == '__main__':
    main()
