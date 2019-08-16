#!/usr/bin/env python3

from timeit import timeit
from os import path
from argparse import ArgumentParser

# This Python implementation does the exact same thing with a buffer, but in Python, so it is much slower.

parser = ArgumentParser()
parser.add_argument("filename", help="the name of the file used")
filename = parser.parse_args().filename

def main():
    total = 0
    size = path.getsize(filename)
    buffersize = 1024*1024

    with open(filename) as f:
        while True:
            c = f.read(buffersize)
            if not c:
                break
            for digit in c:
                if int(digit)%2 : total += 1

    print(f"Total: {total}")
    print(f"Filesize: {size}")
    print(f"Ratio: {total/size}")

print(f"Elapsed time: {timeit(lambda: main(), number = 1):.6f} s")