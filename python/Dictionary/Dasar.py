mhs = {1001:"Aji", 1002:"Gelar", 1003:"Prayogo"}
print()

print("1001:Aji, 1002:Gelar, 1003:Prayogo")
print("Untuk Lebih Lanjut, Cek Text Editor")

print("Output Dari 1001")
print(mhs[1001])
print()

print("Menampilkan Daftar Keys")
print(mhs.keys())
print()

print("Menampilkan Daftar Nilai")
print(mhs.values())
print()

print("Mengubah Data 1002 Dari Gelar Ke Ngeh")
print("Sebelum Diubah : ")
print(mhs[1002])
mhs.update({1002:"Ngeh"})
print("Setelah Diubah : ")
print(mhs[1002])
print()

print("Menghapus Data")
print("Sebelum Dihapus : ")
print(mhs[1003])
print("Setelah Dihapus : ")
del mhs[1003]
print(mhs[1003])
print("Error Karena Datanya Tidak Ada")
print()
