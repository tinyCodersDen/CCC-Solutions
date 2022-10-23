import string
cipher = input('')
encoder = input('')
cipher2 = []
l = list(string.ascii_lowercase)
for zxc in list(string.ascii_lowercase):
  l.append(zxc)
encoded_message = ''
final_text = ''
for z in cipher.lower():
  cipher2.append(ord(z)-97)
encoder = encoder.lower()
for q in encoder:
  if q in string.ascii_lowercase:
    encoded_message+=q
c = 0
for i in encoded_message:
  final_text+=l[l.index(i)+cipher2[c]]
  c+=1
  if c==len(cipher2):
    c=0
print(final_text.upper())

