exec('a = 5')
print(a)

from math import *
while 1:
	b = input('Input : ')
	if b =='':
		break
	exec('Inputan = '+b)
	print('Anda Memasukkan :',Inputan)