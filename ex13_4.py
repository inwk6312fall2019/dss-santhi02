from string import punctuation, whitespace

origin = 'origin.txt' # Origin of Species, 1859
huck = 'huck.txt' # Huck Finn, 1884
don = 'don.txt' # Don Quixote, 1605
great = 'great.txt' # Expectations, 1860
meta = 'meta.txt' # morphisis, 1915
sherlock = 'sherlock.txt' # 1887
divine = 'divine.txt' # Comedy, 1308
journey = 'journey.txt'  # to the center of the earth, 1864

word_file = 'words.txt'
books = 'book.txt'

def words(book):
    list_ = []
    flag = False
    signal = "*** START OF"
    for line in book:
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    return list_
    
def clean(word):
    result = ''
    for char in word:
        if (char in whitespace) or (char in punctuation):
            pass
        elif not char.isalpha():
            pass
        else:
            result += char.lower()
    return result

def stats():
    for book in books:
        book_words = set([clean(word) for word in words(open(book, 'r'))])
        words_ = set([word for word in open(word_file, 'r')])
        print ("Stats for %s" % open(book, 'r').name)
        print ("  There are %s non-listed words." % len(book_words - words_))
        
stats()

print ("\n\nThe words not in the word list for origin.txt:")
print (set([clean(word) for word in words(open(origin, 'r'))])- set([word for word in open(word_file, 'r')]))
