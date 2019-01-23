def jumlah():
	huruf = {}
	for h in nama:
		if huruf==(h):
			jml = huruf[h]+1
		else:
			jml = 1
		huruf.update({h:jml})
	return huruf
nama = input('Masukkan Nama Anda : ')
print (jumlah())