text="ABABBCCD"
frequency_count={num:text.count(num) for num in text}
print(frequency_count)
for k,v in frequency_count.items():
    if v==1:
      print(k)