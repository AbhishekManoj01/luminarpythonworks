text="pneumonoultramicroscopicsilicovolcanoconiosis"
v_count=0
c_count=0
vowels="aeiou"
for i in text:
    if i=="a" or i=="e" or i=="i"or i=="o" or i=="u" :
     v_count=v_count+1
    else:
       c_count=c_count+1
print("vowel count",v_count)
print("cosonent count",c_count)