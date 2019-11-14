print("Baca Tulis File")
print("Menulis Sebuah Teks Nama Ane Ke Txt Ngeh")
f = open("ngeh.txt", "w")
f.write("Aji Gelar Prayogo\n")
f.write("1700018016")
f.close()
print("Mengakhiri Fungsi Tulis File")
print()
print("Membaca File Ngeh.txt")
f = open("ngeh.txt", "r")
for baris in f.readlines():
    print(baris)
#The readlines() method returns a list containing each line in the file as a list item
print()