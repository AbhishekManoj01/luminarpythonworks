from json import load
f=open("C:\\Users\\ASUS\\Desktop\\Pythonworks\\fileinput\\dataset\\books.json")
data=load(f)
#for book in data:
    #print(book)
# title=[book.get("title" )for book in data]
# for b in title:
#  print(b)
               #books with page <250
page_filter=[book.get("title") for book in data if book.get("pages")<250]
#print(page_filter)

                #print all jenre
generes=[book.get("genre") for book in data]
#print(set(generes))
        
genere_count={genre:generes.count(genre) for genre in generes }
#print(genere_count)
         #print costly book

costly_book=max(data,key=lambda d:d.get("price"))
#print(costly_book)
    #author with more than one book
authors=[book.get("author") for book in data ]
count={aut:authors.count(aut) for aut in authors}
k=([k for k,v in count.items() if v>1])
print(k)