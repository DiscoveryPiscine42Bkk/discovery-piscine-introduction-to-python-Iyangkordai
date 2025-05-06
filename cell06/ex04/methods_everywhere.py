#!/usr/bin/env python3

import sys

arg = sys.argv
check = len(arg)
class change:
    def shrink(self,text):
        print(text[slice(0,8)])
    def enlarge(self,text):
        lenge = len(text)
        while lenge < 8:
            text = text+"Z"
            lenge += 1
        print(text)

if check <=1 :
    print("none")
else:
    obj = change()
    for i in range(1,check):
        if len(arg[i]) < 8:
            obj.enlarge(arg[i])
        else:
            obj.shrink(arg[i])
