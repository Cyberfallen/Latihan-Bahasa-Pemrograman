print "Program Untuk Mengetahui Key"
print "Cek Nano Untuk Lebih Lanjut"
print "Data : 1998:Aji Gelar, 2000:N, 1996:M"
print "Data A = 7.7"
manusia = {1998:"Aji Gelar",2000:"N",1996:"M"}
a = 7.7
b = []
print "Mencetak Data Yang Tahun 2000"
print manusia[2000]

print "Daftar Kunci"
print manusia.keys()

print "Daftar Nilai"
print manusia.values()

print "Update Data 1998 Ke Aji"
manusia.update({1998:'Aji'})
print manusia

print "Menghapus Data 1998"
del manusia[1998]
print manusia

print "Mengetahui Tipe Data 2000 & A"
print type(2000)
print type(a)

print "Daftar Fungsi Suatu Objek, Cek Nano"
#print dir(b)
