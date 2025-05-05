#!/usr/bin/env python3

x = int(input())
if x > 25:
    print("Error")
else:
    while(x <=25):
        print(f"Inside the loop, my variable is {x}")
        x += 1
    