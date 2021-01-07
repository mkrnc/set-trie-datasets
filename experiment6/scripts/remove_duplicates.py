#!/usr/local/bin/python3

import sys

def remove_duplicates(file_in):
    distinctLines = {}
    with open(file_in, "r") as f:
        for line in f:
            if line in distinctLines:
                distinctLines[line] += 1
            else:
                distinctLines[line] = 0
    with open(file_in + ".distinct", "w") as f:
        for set in distinctLines:
            f.write(set)

remove_duplicates(sys.argv[1])
