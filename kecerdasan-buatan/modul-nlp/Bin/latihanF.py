import re

# Teks sumber
baris = open("kata.txt", "r")
isi_baris = baris.read()
print(isi_baris)


# Menggunakan re.findall() untuk mendapatkan jumlah token
tokens = re.findall(r'\w+|\S\w*', isi_baris)

# Hitung jumlah token
jumlah_token = len(tokens)

# Cetak output
print(f"Jumlah kata (token): {jumlah_token}")
print(f"Kata-kata (token) hasil RegEx: {tokens}")
baris.close()