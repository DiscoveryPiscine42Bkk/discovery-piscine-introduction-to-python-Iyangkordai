#!/usr/bin/env python3

for i in range(0,11):
    print(f"Table de {i}: ",  end="")
    for y in range(0,11):
        print(f"{ i* y}",sep=" ")
        y+=1
    i += 1
        