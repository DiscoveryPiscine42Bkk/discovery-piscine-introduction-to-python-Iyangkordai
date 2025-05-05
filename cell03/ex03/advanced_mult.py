#!/usr/bin/env python3

for i in range(0,11):
    print(f"Table de {i}: ",  end="")
    for y in range(0,11):
        if y != 10:
            print(f"{i*y}" , end=" ")
        else:
            print(i*y)
         