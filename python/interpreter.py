print("Interpreter")
print("exec=5")
exec("a=5")
print(a)
print()

print("Menerima Inputan, Apabila Input = Enter(Kosong), Maka Inputan Selesai, HANYA ANGKA")
from math import *

while 1:
    r = input("x = ")
    if r == "":
        break
    exec("x = " + r)
    print(x)