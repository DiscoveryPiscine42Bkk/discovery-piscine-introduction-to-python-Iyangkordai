#!/usr/bin/env python3

import sys 
arg = sys.argv
check = len(arg)

if check != 2:
    print("none")
else:
    print(arg[1].upper())
