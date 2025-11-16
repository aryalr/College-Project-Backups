import re
word = 'supercalifragilisticexpialidocious' 
stem = re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes')
print(stem)
