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
            if y != 10:
                print(f"{i*y}" , end=" ")
            else:
                print(i*y)
            y += 1
        i += 1
         