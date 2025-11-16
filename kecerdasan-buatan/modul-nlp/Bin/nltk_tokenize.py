text = "Saya belajar bahasa pemrogramman karena komputer tidak bicara bahasa inggris. awikwok"

from nltk.tokenize import word_tokenize 
import string
tokens = word_tokenize(text) 
punctuations = string.punctuation

words = [word for word in tokens if word not in punctuations]
print(len(words), "kata kata tanpa tanda baca: ", words)