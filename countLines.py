import os
import sys


filename = '/etc/passwd'
# filename = str(sys.argv[1])
nLines = 0

f = open(filename, 'r')
for line in f:
    nLines += 1
f.close()

print(nLines)
