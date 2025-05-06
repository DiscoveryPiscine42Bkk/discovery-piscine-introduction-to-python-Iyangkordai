#!/usr/bin/env python3

class greet:
    def greeting(self,guess = "noble stranger"):
        if isinstance(guess,str):
            print(f"Hello, {guess}")
        else:
            print("Error! It was not a name.")

obj = greet()
obj.greeting("Alexandra")
obj.greeting("Will")
obj.greeting()
obj.greeting(42)
