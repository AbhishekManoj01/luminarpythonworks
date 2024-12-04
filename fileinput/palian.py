word_ref=open("C:\\Users\\ASUS\\Desktop\\Pythonworks\\fileinput\\dataset\\words.txt")
palian_ref=open("C:\\Users\\ASUS\\Desktop\\Pythonworks\\fileinput\\dataset\\palian_words.txt","w")
reverse=""
for line in word_ref:
    word=line.strip("\n")
    reverse=word[::-1]
    if word==reverse:
        palian_ref.write(word+"\n")
palian_ref.close()