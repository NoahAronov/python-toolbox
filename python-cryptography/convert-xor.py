# Created while participating in course: CryptoHack.org 

text = 'label'

result = ''
for n in text:
    result += chr(ord(n) ^ 13)

print(f"crypto{{{result}}}")