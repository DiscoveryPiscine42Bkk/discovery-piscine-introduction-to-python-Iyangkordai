#!/usr/bin/env python3

password = "Python is awesome"

x = input()
if x == password:
    print("ACCESS GRANTED")
elif x != password:
    print("ACCESS DENIED")