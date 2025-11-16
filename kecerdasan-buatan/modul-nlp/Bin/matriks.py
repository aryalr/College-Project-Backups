import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 


def _create_frequency_matrix(sentences):
    frequency_matrix = {}
    
    # Inisialisasi Stopwords dan Stemmer
    # Menggunakan stopwords Bahasa Indonesia
    stopWords = set(stopwords.words("indonesian"))
    ps = PorterStemmer() # Stemmer Bahasa Inggris

    for sent in sentences:
        freq_table = {}
        # Tokenisasi kalimat menjadi kata-kata
        words = word_tokenize(sent)
        
        for word in words:
            word = word.lower()
            # Lakukan stemming
            word = ps.stem(word)
            
            # Lewati (continue) jika kata adalah stopwords
            if word in stopWords:
                continue
            
            # Hitung frekuensi
            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1
        
        # Simpan tabel frekuensi, menggunakan 15 karakter pertama kalimat sebagai kunci
        frequency_matrix[sent[:15]] = freq_table
        
    return frequency_matrix

# --- Contoh Penggunaan ---
# Definisikan variabel sentences (Harus berupa daftar/list)
sentences = [
    "Indonesia merdeka pada tanggal 17 Agustus.",
    "Banyak upaya telah dilakukan untuk merespons pandemi.",
    "Pemerintah dan UNICEF bekerja sama."
]

# Panggil fungsi
freq_matrix = _create_frequency_matrix(sentences)

# Cetak output
print(freq_matrix)