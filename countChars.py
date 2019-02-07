import os
import sys
# from sys import getsizeof


filename = '/etc/passwd'
# filename = str(sys.argv[1])

f = open(filename, 'r')
text = f.read()
f.close()

nChars = len(text)
print(nChars)

# num_bytes = getsizeof(text)
# print(num_bytes)
