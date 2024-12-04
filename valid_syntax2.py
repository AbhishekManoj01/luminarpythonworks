user_input=input("Enter the bracket pairs :")
symbol_dictionary={"{":"}",
                   "[":"]",
                   "(":")",
                   "<":">"}
symbol_stack=[]
top=-1
is_valid=True
for ch in user_input:
    if ch in symbol_dictionary:
        top+=1
        symbol_stack.append(ch)
    elif len(symbol_stack)!=0 and ch==symbol_dictionary.get(symbol_stack[top]):
        top-=1
        symbol_stack.pop()
    else:
        is_valid=False
print("valid" if len(symbol_stack)==0 and is_valid==True else "not valid")