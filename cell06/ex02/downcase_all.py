#!/usr/bin/env python3

import sys
arg = sys.argv
check = len(arg)

class lower:
    def dowcase_it(self,text):
        ans = str(text)
        ans = ans.lower()
        return ans

if check <= 1:
    print("none")
else:
    obj = lower()
    for i in range(1,check):
        print(obj.dowcase_it(arg[i]))
