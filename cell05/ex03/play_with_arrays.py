#!/usr/bin/env python3 

old = [2,8,9,48,8,22,-12,2]
new = []
new_set = {}
for i in old:
    now = i+2
    if now >= 5:
        new.append(i+2)
    else:
        continue
new_set = set(new)
print(f"Original array : {old}")
print(f"New array: {new_set}")
