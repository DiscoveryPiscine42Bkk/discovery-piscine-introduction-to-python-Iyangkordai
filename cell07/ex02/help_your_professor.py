#!/usr/bin/env python3

class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}
class score:
    def average(self,dict):
        score_s = list(dict.values())
        sum = 0
        for i in range(0,len(score_s)):
            now = int(score_s[i])
            sum += now
        ans = sum / len(score_s)
        return ans
obj = score()
print(f"Average for class 3B: {obj.average(class_3B)}")
print(f"Average for class 3C: {obj.average(class_3C)}")
