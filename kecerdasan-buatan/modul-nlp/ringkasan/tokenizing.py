import math
import string
import sys
import os

# Import NLTK Components
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

# --- 1. Persiapan Data ---
skrip_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(skrip_dir, "text_str.txt")

# Membaca teks string dari file text_str.txt
try:
    with open(file_path, "r", encoding="utf-8") as file:
        teks = file.read()
except FileNotFoundError:
    print("❌ ERROR: File 'text_str.txt' tidak ditemukan. Mohon sediakan file tersebut.")
    sys.exit(1)

# Tokenisasi ke dalam kalimat
sentences = sent_tokenize(teks)
total_documents = len(sentences)

# --- 2. FUNGSI: Matriks Frekuensi Mentah ---
def _create_frequency_matrix(sentences):
    frequency_matrix = {}
    stopWords = set(stopwords.words("indonesian"))
    ps = PorterStemmer() 
    for sent in sentences:
        freq_table = {}
        words = word_tokenize(sent)
        for word in words:
            word = word.lower()
            if all(char in string.punctuation for char in word):
                continue
            stemmed_word = ps.stem(word)
            if stemmed_word in stopWords:
                continue
            freq_table[stemmed_word] = freq_table.get(stemmed_word, 0) + 1
        frequency_matrix[sent[:15]] = freq_table 
    return frequency_matrix

# --- 3. FUNGSI: Matriks Term Frequency (TF) ---
def _create_tf_matrix(freq_matrix):
    tf_matrix = {}
    for sent, f_table in freq_matrix.items():
        tf_table = {}
        count_words_in_sentence = sum(f_table.values()) 
        if count_words_in_sentence == 0:
            tf_matrix[sent] = {}
            continue
        for word, count in f_table.items():
            tf_table[word] = count / count_words_in_sentence
        tf_matrix[sent] = tf_table
    return tf_matrix

# --- 4. FUNGSI: Menghitung Document Frequency (DF) ---
def _create_documents_per_words(freq_matrix):
    word_per_doc_table = {}
    for sent, f_table in freq_matrix.items():
        for word in f_table.keys():
            word_per_doc_table[word] = word_per_doc_table.get(word, 0) + 1
    return word_per_doc_table

# --- 5. FUNGSI: Membuat Matriks Inverse Document Frequency (IDF) ---
def _create_idf_matrix(freq_matrix, count_doc_per_words, total_documents):
    idf_matrix = {}
    for sent, f_table in freq_matrix.items():
        idf_table = {}
        for word in f_table.keys():
            idf_table[word] = math.log10(total_documents / float(count_doc_per_words[word]))
        idf_matrix[sent] = idf_table
    return idf_matrix

# --- 6. FUNGSI: Membuat Matriks TF-IDF ---
def _create_tf_idf_matrix(tf_matrix, idf_matrix):
    tf_idf_matrix = {}
    for sent, tf_table in tf_matrix.items():
        tf_idf_table = {}
        idf_table = idf_matrix.get(sent, {})
        for word, tf_value in tf_table.items():
            idf_value = idf_table.get(word, 0.0)
            tf_idf_table[word] = float(tf_value * idf_value) 
        tf_idf_matrix[sent] = tf_idf_table
    return tf_idf_matrix

# --- 7. FUNGSI: Menghitung Skor Kalimat ---
def _score_sentences(tf_idf_matrix) -> dict:
    sentenceValue = {}
    for sent, f_table in tf_idf_matrix.items():
        total_score_per_sentence = 0
        count_words_in_sentence = len(f_table)
        if count_words_in_sentence == 0:
            sentenceValue[sent] = 0.0
            continue
        for score in f_table.values():
            total_score_per_sentence += score
        sentenceValue[sent] = total_score_per_sentence / count_words_in_sentence
    return sentenceValue

# --- 8. FUNGSI: Menghitung Skor Rata-rata (Threshold) ---
def _find_average_score(sentenceValue) -> float:
    sumValues = 0.0
    if not sentenceValue:
        return 0.0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]
    average = (sumValues / len(sentenceValue)) 
    return average

# --- 9. FUNGSI: Menghasilkan Ringkasan ---
def _generate_summary(sentences, sentenceValue, threshold):
    """
    Menghasilkan ringkasan dengan memilih kalimat yang skornya di atas ambang batas.
    """
    summary = ''
    sentence_count = 0
    
    # Perulangan melalui kalimat asli
    for sentence in sentences:
        # Kunci (key) yang digunakan adalah 15 karakter pertama kalimat asli
        key = sentence[:15]
        
        # Cek apakah kalimat ada di dictionary dan skornya MELEBIHI threshold
        if key in sentenceValue and sentenceValue[key] >= threshold:
            # Tambahkan kalimat asli (belum di-stemming/dibersihkan) ke ringkasan
            summary += " " + sentence 
            sentence_count += 1
            
    return summary

# --- EKSEKUSI DAN HASIL ---

# Proses TF-IDF dan Skor
freq_matrix = _create_frequency_matrix(sentences)
count_doc_per_words = _create_documents_per_words(freq_matrix)
tf_matrix = _create_tf_matrix(freq_matrix)
idf_matrix = _create_idf_matrix(freq_matrix, count_doc_per_words, total_documents)
tf_idf_matrix = _create_tf_idf_matrix(tf_matrix, idf_matrix)
sentence_scores = _score_sentences(tf_idf_matrix)
threshold = _find_average_score(sentence_scores)

# Menghasilkan Ringkasan
# Menggunakan 1.3 * threshold untuk ambang batas yang lebih ketat
summary = _generate_summary(sentences, sentence_scores, 1.3 * threshold)

print(f"\nTotal Kalimat Asli: {total_documents}")
print(f"Ambang Batas (Threshold) Dasar: {threshold:.4f}")
print(f"Ambang Batas yang Digunakan (1.3 * Threshold): {1.3 * threshold:.4f}")
print("\n--- RINGKASAN YANG DIHASILKAN ---")
print(summary.strip())