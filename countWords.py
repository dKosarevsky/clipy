import os
import sys


filename = '/etc/passwd'
# filename = str(sys.argv[1])

f = open(filename, 'r')
text = f.read()
f.close()

list_words = text.split(None)
nWords = len(list_words)

print(nWords)
