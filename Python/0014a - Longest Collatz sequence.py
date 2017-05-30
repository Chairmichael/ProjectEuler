'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 	(n is even)
n → 3n + 1 	(n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def collatz(n, seq):
	if n == 1: 
		seq.append(n)
		return seq
	else:
		seq.append(n)
		if n%2 == 0:
			n = int(n/2)
			return collatz( n, seq )
		else:
			n = int(3*n + 1)
			return collatz( n, seq )

end = int(1e6)
max_seq = [ ]
for start in range(1, end):
	seq = collatz(start, [])
	if len(seq) > len(max_seq):
		max_seq = seq
print(max_seq)
print(len(max_seq))
