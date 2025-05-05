#!/usr/bin/env python3

x = int(input("Enter the first number: \n"))
y = int(input("Enter the second number: \n"))
ans2 = ""
ans = x * y
if ans < 0:
    ans2 = "negative."
elif ans > 0:
    ans2 = "positive."
elif ans == 0:
    ans2 = "positive and negative."
print(f"{x} x {y} = {ans}\nThe result is {ans2}")