#!/usr/bin/env python3

import sys 
arg = sys.argv
check  = len(arg)
if check < 3:
    print("none")
else:
    for i in range(check - 1,0,-1):
        print(arg[i])
