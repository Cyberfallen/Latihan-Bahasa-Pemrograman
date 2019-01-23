print ("Pelatihan Fungsi")
def garis():
	print ('-'*100)
garis()
def garis(a):
	print ('-'*a)
print ("Diketahui Sisi = 7")
def luas_persegi(sisi)	:
	luas = sisi*sisi
	return luas

print ("Luas Persegi Adalah : %d" %luas_persegi(7))

#def tambah(a,b):
	#a = input("Masukkan Angka Pertama :")
	#b = input("Masukkan Angka Kedua :")
	#return a+b
	#print (tambah())

print('Angka = 5')
def faktorial(n):
	if n<=1:
		return 1
	else:
		return n*faktorial(n-1)
print (faktorial(5))