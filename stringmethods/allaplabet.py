text="The quivk brown fox jumps over the lazy dog"
alphabet="abcdefghijklmnopqrstuvwxyz"
is_pangram=True
for ch in alphabet:
    if ch not in text:
      is_pangram=False
      break
print("ispangram")