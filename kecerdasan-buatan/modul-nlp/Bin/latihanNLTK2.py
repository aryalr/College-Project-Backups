import nltk
from nltk.corpus import reuters

# 1. Menampilkan file ID yang mengandung kategori 'yen'
print("File IDs dengan kategori 'yen':")
print(reuters.fileids('yen')) 

#-----------------

# 2. Mengambil 14 kata pertama dari file 'training/6357'
print("\n14 kata pertama dari 'training/6357':")
print(reuters.words('training/6357')[:14])