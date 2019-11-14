print("Exception(Untuk Menangkap Sebuah Kesalahan)")
n = input("Mencari Akar n, n = ")
try:
    print(float(n) ** 0.5)
except:
    print(n, "Bukan Angka")