import os
import sys
import argparse


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

if args.filenames == None:
    print('No filenames given!')
else:
    for f in args.filenames:
        print(f)

if args.m == True:
    print('-m is on!')
else:
    print('-m is off!')

if args.l == True:
    print('-l is on!')
else:
    print('-l is off!')

if args.w == True:
    print('-w is on!')
else:
    print('-w is off!')

if args.c == True:
    print('-c is on!')
else:
    print('-c is off!')
