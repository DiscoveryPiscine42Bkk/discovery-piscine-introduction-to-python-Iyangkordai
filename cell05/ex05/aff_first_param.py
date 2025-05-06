#!/usr/bin/env python3

import sys 
arg = sys.argv
check = len(arg)
if check <= 1:
    print("none")
else:
    print(f"{arg[1]}")
