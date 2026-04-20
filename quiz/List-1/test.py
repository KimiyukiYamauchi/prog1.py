#!/usr/bin/env python

def print_upto(num):
    for i in range(num):
        print(i)

import sys
print_upto(int(sys.argv[1]))
