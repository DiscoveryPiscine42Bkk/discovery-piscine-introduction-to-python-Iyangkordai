#!/usr/bin/env python3

import sys 
import re
arg = sys.argv
check  = len(arg)
array = []
if check < 2:
    print("none")
else:
    for i in range(1,check):
        now = len(arg[i])
        if re.search("ism$",arg[i]):
            continue
        else:
            print(f"{arg[i]}ism")

