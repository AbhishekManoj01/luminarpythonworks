num=input("Enter the number :")
length=len(num)
l=length
string=""

num_dict={"0":"Zero","1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine"}
hundred_dict={"1":"one hundred","2":"Two hundred","3":"Three hundred","4":"Four hundred","5":"Five hundred","6":"Six hundred","7":"Seven hundred","8":"Eight hundred"}
tens_dict={"2":" twenty ","3":" thirty ","4":" forty ","5":" fifty ","6":" sixty ","7":" seventy ","8":" eighty "}
ones_case={"11":"eleven","12":"twelve","13":"thirteen","14":"fourteen","15":"fifteen","16":"sixteen","17":"seventeen","18":"eighteen","19":"nineteen"}
for i in range(length):
    if l==3 and num[i] in hundred_dict:
        string=string+hundred_dict.get(num[i])
        string+=" and"
    if l==2:
        if num[i]==1:
            ch=""
            ch+=num[i]
            ch+=num[i+1]
            string+=ones_case.get(ch)
            break
        else:
            string+=tens_dict.get(num[i])
    if l==1 and num[i] in num_dict:
        string+=num_dict.get(num[i])
    l-=1

print(string)
