user_input=input("Enter bracket pairs :")
symbol_stack=[]
opens_list=["{","[","(","<"]
close_list=["}","]",")",">"]
is_balanced=True
for ch in user_input:
    if ch in opens_list:
        symbol_stack.append(ch)
    elif ch in close_list:
        ind=close_list.index(ch)
        if len(symbol_stack)>0 and opens_list[ind]==symbol_stack[len(symbol_stack)-1]:
            symbol_stack.pop()
        else:
            is_balanced=False
            break
print("Balanced" if is_balanced==True else "Not balanced")