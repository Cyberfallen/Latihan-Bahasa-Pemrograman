from math import *

while 1:
    r = input("x = ")
    if r == "":
        break
    exec("x = " + r)
    print(x)