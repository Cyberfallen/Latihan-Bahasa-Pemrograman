print("Fungsi untuk printer")
print("LINUX User")
#Sebuah printer dapat dianggap sebuah file, biasanya
#ada di /dev/lp0(Untuk Linux)
f = open("/dev/lp0", "w")
f.write("Test\n")
f.close()
print()

#su -c "chmod 666 /dev/lp0"
#Untuk Memiliki Hak Tulis Pada /dev/lp0

print("Ukuran Huruf")
#Sertakan chr(15) pada awal percetakan untuk memper
#kecil ukuran huruf, dan ini cukup digunakan sekali
#
f = open("/dev/lp0","w")
f.write(chr(15))
f.close()
print()

#cat /etc/hosts > /dev/lp0

print("Ganti Halaman")
#Mengganti halaman Bisa Juga Diartikan Mengeluarkan
#Kertas dari printer. Untuk kertas continues, mengg
#anti halaman berarti menuju ke lembar selanjutnya
f = open("dev/lp0","w")
f.write("\f")
f.close()
print()