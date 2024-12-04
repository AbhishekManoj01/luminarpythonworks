text="hello hai morning"
words=text.split(" ")
# def  get_length(w):
#     return len(w)
# srt_words=sorted(words,key=get_length,reverse=True)
srt_words=sorted(words,key=lambda w:len(w),reverse=True)
print(srt_words)