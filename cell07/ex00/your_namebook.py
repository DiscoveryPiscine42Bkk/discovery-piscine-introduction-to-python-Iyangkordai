#!/usr/bin/env python3
ans = []
person = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
class name:
    def array_of_name(self,name,lastname):
        name = str(name).capitalize()
        lastname = str(lastname).capitalize()
        ans.append(f"{name} {lastname}")
first_n =list(person.keys())
last_n = list(person.values())
obj = name()
for i in range(0,len(person)):
    obj.array_of_name(first_n[i], last_n[i])
print(ans)
