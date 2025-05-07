#!/usr/bin/env python3

class x:
    def smt(self,a):
        a += 1
        print(f"This is a in method : {a}")

obj = x()
a = 2
obj.smt(a)
print(f"This is a out method : {a}")
