import nltk
from nltk.stem import PorterStemmer, LancasterStemmer
from nltk.tokenize import word_tokenize

raw = """DENNIS: Listen, strange women lying in ponds distributing swords ... is no basis for a system of government. Supreme executive power derives from ... a mandate from the masses, not from some farcical aquatic ceremony."""

# Tokenisasi
token = word_tokenize(raw)

# Inisialisasi Stemmer
porter = PorterStemmer()
lancaster = LancasterStemmer()

# Lakukan Stemming dengan Porter
porter_stems = [porter.stem(t) for t in token]

# Lakukan Stemming dengan Lancaster
lancaster_stems = [lancaster.stem(t) for t in token]

## Cetak Hasil untuk Perbandingan
print("Original Tokens:", token[:10])
print("-" * 50)
print("Porter Stems: ", porter_stems[:10])
print("Lancaster Stems:", lancaster_stems[:10])

# Cetak perbandingan lengkap (Opsional, menggunakan zip)
print("\nKata Asli | Porter Stem | Lancaster Stem")
print("-" * 50)
for original, p_stem, l_stem in zip(token, porter_stems, lancaster_stems):
    print(f"{original:11} | {p_stem:11} | {l_stem:11}")