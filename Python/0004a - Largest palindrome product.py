'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

nums = []
for a in range(100, 1000):
	for b in range(100, 1000):
		c = str(a*b)
		if c == c[::-1]:
			nums.append([a*b, a, b])
print('{} = {} * {}'.format(max(nums)[0], max(nums)[1], max(nums)[2]))