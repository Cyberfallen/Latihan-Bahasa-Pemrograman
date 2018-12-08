print "Program Untuk Menyalin Suatu Variabel List Ke Variabel Lainnya"
print "Program Ini Jauh Lebih Berguna Di Terminal Python"
print "Data : 1,2,3,4"
a = [1,2,3,4]
#B Seharusnya Tidak Perlu Dideklarasikan
b = [0]
a = b
print "Data2 = Data"
print "Dimana Data Ke-2 Sama Dengan Data-1"
print "Data : 1"
print a
print "Data : 2"
print b
print "Proses Listing"
b = list(a)
a.append(99)
print a
print b
