import sys
import string

namafile = sys.argv[0]
print(namafile)
print( "-" * len (namafile) )

file = open(namafile, "r")
jumlahbaris = len(file.readlines())
lebar = len(str(jumlahbaris))
file.seek(0)
n = 0
for baris in file.readlines():
    n = n+1
    nomor = str.zfill(n, lebar)
    print ("%s | %s" % (nomor, baris)),
file.close()

#Fungsi zfill Untuk memenuhi Suatu Angka Atau String Dengan "0" alias zerofill