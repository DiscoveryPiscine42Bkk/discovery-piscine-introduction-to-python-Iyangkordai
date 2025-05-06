#!/usr/bin/env python3
dupout_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}
ans = []
class red:
    def find_the_redheads(self,dict):
        filter_dict = {k: v for k, v in dict.items() if v == 'red'}
        name = list(filter_dict.keys())
        return name
family = red()
print(family.find_the_redheads(dupout_family))
