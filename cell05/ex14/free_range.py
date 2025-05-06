#!/usr/bin/env python3

import sys
arg = sys.argv
check = len(arg)
array = []
if check != 3 :
    print("none")
else:
    start = int(arg[1])
    end = int(arg[2])
    for i in range(start,end+1):
        array.append(i)
    print(array)
