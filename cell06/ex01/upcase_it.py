#!/usr/bin/env python3

class upcase:
    def upcase_it(self,variable):
        text = str(variable)
        text = text.upper()
        return text

obj = upcase()
print(obj.upcase_it("hello"))
