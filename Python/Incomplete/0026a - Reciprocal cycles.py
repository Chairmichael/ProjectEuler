#/usr/bin/env 
# 0026a - Reciprocal cycles.py

'''

'''

# generates reciprocals of the natural numbers
def nat_rcp():
	n = 1
	while 1:
		yield n, format(1/n, '54f')
		n += 1

def principal_period(s):
    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]

def main():
	for i, n in nat_rcp():
		p = principal_period(str(n))
		if i > 100:# or p is None:
			break
		else:
			print(i, n, p)
		


if __name__ == '__main__':
	main()
