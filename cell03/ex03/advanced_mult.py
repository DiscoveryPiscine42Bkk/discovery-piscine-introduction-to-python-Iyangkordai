#!/usr/bin/env python3
import sys
arg = sys.argv
i = 0
y = 0
if len(arg) > 1:
    print("none")
else:
    while i < 11:
        print(f"Table de {i}: ",  end="")
        y = 0
        while y < 11:
            print(f"{i*y}" , end=" ")
            y += 1
        print("")
        i += 1
         