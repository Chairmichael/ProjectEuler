'''
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position 
in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

def word_score(s):
	return sum([ord(c) - 64 for c in s])

def name_list_score(l):
	l.sort()
	scores = [ ]
	for i, e in enumerate(l):
		scores.append(i+1 * word_score(e))
	print(sum(scores))

def main():
	names = [ ]
	with open('p022_names.txt') as data:
		names = [s[1:-1] for s in data.read().split(',')]
	name_list_score(names)

if __name__ == '__main__':
	main()