#!/usr/bin/env python3 

first_num = int(input("Give me the first number: "))
second_num = int(input("Give me the second number: "))
print("Thank you")
opt = ["+","-","/","*"]
ans = [first_num + second_num , first_num - second_num , int(first_num / second_num) , first_num * second_num]
for i in range(0,4):
    print(f"{first_num} {opt[i]} {second_num} = {ans[i]}")
