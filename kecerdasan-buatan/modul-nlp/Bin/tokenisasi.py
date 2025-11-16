import re

raw = """'When I'M a Duchess,' she said to herself, (not in a very hopeful tone though), 'I won't have any pepper in my kitchen AT ALL. Soup does very well without--Maybe it's always pepper that makes people hot-tempered,'..."""

token = re.split(r' ', raw)
tokentab = re.split(r'[ \t\n]+', raw)
print(tokentab)