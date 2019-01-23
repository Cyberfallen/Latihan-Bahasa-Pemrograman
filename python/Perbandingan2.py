print ("Perbandingan")
a = int(input("Masukkan Umur Anda : "))
if a == 18 or a >18	:		#Singkatnya =>18
	print ("Anda Telah Dewasa")
elif a<18		:
	print ("Anda Masih Muda")
else			:
	print ("Inputan Tidak Sesuai")

y = float(input("Masukkan Inputan Angka Pertama : "))
z = float(input("Masukkan Inputan Angka Kedua : "))
if y<z	:
	print ("Angka Pertama Lebih kecil Daripada Angka Kedua")
elif y>z:
	print ("Angka Pertama Lebih Besar Daripada Angka Kedua")
elif y==z:
	print ("Angka Pertama Sama Dengan Angka Kedua")
else:
	print ("Something Wrong")