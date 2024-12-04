text="ABAABBC"
#most recursive chsracter
print(max(text,key=lambda ch:text.count(ch)))
#least recursive character
print(min(text,key=lambda ch:text.count(ch)))