#!/usr/bin/env python3

import sys 
import re

arg = sys.argv
check = len(arg)

if check != 3:
    print("none")
else:
    cnt = len(re.findall(arg[1],arg[2]))
    print(cnt)

