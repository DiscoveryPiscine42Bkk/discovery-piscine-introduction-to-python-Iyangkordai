#!/usr/bin/env python3

import sys
arg = sys.argv
check = len(arg) 

if check <= 1:
    print("none")
else:
    print(f"parameters: {check}")
    for i in range(0,check):
        if i == 0:
            continue
        else:
            print(f"{arg[i]}: {len(arg[i])}")
