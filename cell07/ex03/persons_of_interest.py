#!/usr/bin/env python3

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
list_a = []
class women:
    def famous_births(self,dict):
        key = list(dict.keys())
        for i in range(0,len(dict)):
            data = dict[key[i]]
            name = data.get("name")
            list_a.append(name)
            date = data.get("date_of_birth")
            list_a.append(date)
        new = {list_a[i]: list_a[i+1] for i in range(0, len(list_a),2)}
        ans = sorted(new.items(), key=lambda date: date[1])
        for i in range(0,len(ans)):
            print(f"{ans[i][0]} is a great scientist born in {ans[i][1]}.")
obj = women()
obj.famous_births(women_scientists)
