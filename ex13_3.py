from string import punctuation, whitespace
import string

def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d


book = 'book.txt'

with open(book, 'r') as fd:
    words = fd.read().split()

#remove punctuation, whitespace, uppercase
def clean(word):
    cleansed = ''
    for char in word:
        if char in word == string.punctuation:
            pass
        else:
            cleansed += char.lower()
    return cleansed
        
print ("{} has {} 'words'".format(book, len([clean(word) for word in words])))

print(histogram(clean(words)))
