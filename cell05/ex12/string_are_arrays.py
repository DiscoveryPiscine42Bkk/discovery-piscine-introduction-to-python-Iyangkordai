#!/usr/bin/env python3 

import sys
arg = sys.argv
check = len(arg)
count = 0
if check > 1:
    for i in arg[1]:
        if i == 'z':
            count += 1
if count > 0 :
    print('z' * count)
else :
    print("none")