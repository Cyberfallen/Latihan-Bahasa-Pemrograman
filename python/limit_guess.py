username = "ngeh"
inputan = ""
jumlah_inputan = 0
batas_inputan = 3
keluar = False
while inputan != username and not(keluar):
    if jumlah_inputan < batas_inputan:
        inputan = input("Masukkan Kata :")
        jumlah_inputan += 1
    else:
        keluar = True
if keluar:
    print("Sudah 3 Kali")
else:
    print("Berhasil")