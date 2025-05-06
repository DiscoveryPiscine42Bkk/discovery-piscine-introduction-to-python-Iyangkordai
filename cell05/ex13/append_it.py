#!/usr/bin/env python3

import sys

arg = sys.argv
check = len(arg)
word = ["ism"]
if check <=1 :
    print("none")
else:
    for i in range (1, check):
        lenge = len(arg[i])
        now = arg[i][lenge-3:lenge]
        match arg[i]:
            case "ism":
                print(f"{arg[i]}ism")
            case _:
                continue
