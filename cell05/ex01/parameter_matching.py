#!/usr/bin/env python3 

import sys

arg = sys.argv
check = len(arg)
if check <= 1 :
    print("none")
else:
    ans = input("What was the parameter? ")
    if ans == arg[1]:
        print("Good job!")
    else :
        print("Nope, sorry...")
