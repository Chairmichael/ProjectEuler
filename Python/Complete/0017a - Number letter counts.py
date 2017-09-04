'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive 
were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 
342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''
#too ashamed...

teens = [
'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 
'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
numbers = [
['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'],
['', '', 'twenty', 'thirty', 'forty', 'fifty', 
	'sixty', 'seventy', 'eighty', 'ninety'],
['', 'hundred', 'thousand']]

def to_words(num):
	if len(str(num)) == 1: return [ numbers[0][num] ]
	if len(str(num)) == 4: return [ numbers[0][1], numbers[2][2] ]
	words = [ ]
	# reversed string of num, such that s[0]=ones place, s[1]=tens place...
	s = str(num)[::-1]
	# check teens
	if s[1] == '1':
		words.append(teens[ int(s[0]) ])
		if len(s) == 2:
			return words
		else: # 3 digits
			words.insert(0,numbers[0][int(s[2])]) #ones
			words.insert(1,numbers[2][1]) #'hundred'
			words.insert(2,'and')#'and'
	else:
		if len(s) == 2:
			words.append(numbers[1][int(s[1])])#tens
			words.append(numbers[0][int(s[0])])#ones
		elif not num%100:
			words.append(numbers[0][int(s[2])]) #ones
			words.insert(1,numbers[2][1]) #'hundred'
		else: # 3 digits
			words.insert(0,numbers[0][int(s[2])]) #ones
			words.insert(1,numbers[2][1]) #'hundred'
			words.insert(2,'and')#'and'
			words.append(numbers[1][int(s[1])])#tens
			words.append(numbers[0][int(s[0])])#ones

	return words

def main():
	total = 0
	for x in range(1, 1001):
		total += len(''.join(to_words(x)))
	print(total)


if __name__ == '__main__':
	main()