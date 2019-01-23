print("Program Untuk Menghitung Faktorial Suatu Inputan Angka")
angka = int(input("Masukkan Bilangan : "))
faktorial = 1
if angka<0	:
	print("Maaf, Faktorial Tidak Bisa Digunakan Dalam Angka Yang Kurang Dari 0")
elif angka == 0	:
	print("Hasil Faktorialnya Adalah : 1")
else		:
	for i in range(1,angka+1):
		faktorial = faktorial*i
	print("Hasil Faktorialnya Dari",angka,"Adalah",faktorial)