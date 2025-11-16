kalimat = "Berikut ini adalah 5 negara dengan pendidikan terbaik di dunia adalah Korea Selatan, Jepang, Singapura, Hong Kong, dan Finlandia."

lower_case = kalimat.lower() 
#print(lower_case)

import string

kalimat = "Ini &adalah [contoh] kalimat? {dengan} tanda. baca?!!" 
hasil = kalimat.translate(str.maketrans("","",string.punctuation)) 
print(hasil)