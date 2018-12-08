print "Program Untuk Membuat Suatu Kondisi Sekaligus Meneima Inputan"
print "Apa Tipe Gender Anda : "
a = raw_input("L/P : ")
if a == "L" or a == "l" :
	print "Anda Laki-Laki"
elif a == "P" or a == "p" :
	print "Anda Perempuan"
else :
	print "Inputan Tidak Sesuai"

print "Bentuk Logika"
print " "
print "Apakah Anda Siap Belajar Python?"
b = raw_input("y/t : ")
percaya = b =="y"
if percaya :
	print "Anda Siap Menjadi Programmers"
else :
	print "Anda Belum Siap Menjadi Programmers"
