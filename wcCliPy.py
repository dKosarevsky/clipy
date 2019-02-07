import os
import sys
import argparse


def count(filename):

    nLines = 0
    nWords = 0
    nChars = 0
    nBytes = 0

    if filename == None:
        myText = sys.stdin.read()
        chars = len(myText)
        words = len(myText.split())
        lines = len(myText.split('\n'))
        bytes = len(myText.encode('utf-8'))

        return(lines - 1, words, chars, bytes)

    else:
        f = open(filename, 'r')
        for line in f:
            nLines += 1
            nChars = nChars + len(line)
            nWords = nWords + len(line.split())
            nBytes = nBytes + len(line.encode('utf-8'))

        return(nLines, nWords, nChars, nBytes)


def main():

    chars = 0
    words = 0
    lines = 0
    bytes = 0

    totalC = 0
    totalW = 0
    totalL = 0
    totalB = 0

    nFiles = 0

    toPrint = ''

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', default=False, action='store_true',
                        help="Counting Characters", required=False)
    parser.add_argument('-l', default=False, action='store_true',
                        help="Counting Lines", required=False)
    parser.add_argument('-w', default=False, action='store_true',
                        help="Counting Words", required=False)
    parser.add_argument('-c', default=False, action='store_true',
                        help="Counting Bytes", required=False)
    parser.add_argument('filenames', default=None,
                        help="Filenames", nargs='*')

    args = parser.parse_args()

    if args.filenames == []:
        (lines, words, chars, bytes) = count(None)
        if args.l == True:
            toPrint = '{:>8}'.format(lines)
        if args.w == True:
            toPrint = toPrint + '{:>8}'.format(words)
        if args.m == True:
            toPrint = toPrint + '{:>8}'.format(chars)
        if args.c == True:
            toPrint = toPrint + '{:>8}'.format(bytes)
        if args.m == False and args.w == False and args.l == False and args.c == False:
            toPrint = '{:>8}'.format(lines) + '{:>8}'.format(words) + '{:>8}'.format(chars) + '{:>8}'.format(bytes)
        if toPrint != '':
            print(toPrint)
        toPrint = ''

    else:
        for f in args.filenames:
            nFiles = nFiles + 1
            (lines, words, chars, bytes) = count(f)
            totalC = totalC + chars
            totalW = totalW + words
            totalL = totalL + lines
            totalB = totalB + bytes

            if args.l == True:
                toPrint = '{:>8}'.format(lines)
            if args.w == True:
                toPrint = toPrint + '{:>8}'.format(words)
            if args.m == True:
                toPrint = toPrint + '{:>8}'.format(chars)
            if args.c == True:
                toPrint = toPrint + '{:>8}'.format(bytes)
            if args.m == False and args.w == False and args.l == False and args.c == False:
                toPrint = '{:>8}'.format(lines) + '{:>8}'.format(words) + '{:>8}'.format(chars) + '{:>8}'.format(bytes)
            if toPrint != '':
                toPrint = toPrint + '' + '{:>15}'.format(f)
                print(toPrint)
            toPrint = ''

            if nFiles > 1:
                print('{:>8}'.format(totalL) + '{:>8}'.format(totalW) + '{:>8}'.format(totalC) + '{:>8}'.format(totalB) + '' + '{:>15}'.format(' total'))


if __name__ == '__main__':
    main()
else:
    print('This is standalone program, not a module!')
