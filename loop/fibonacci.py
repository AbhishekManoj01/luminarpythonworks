def fibacacci(input): 
 prev=0
 current=1
 print(prev)
 print(current)
 for i in range(1,input+1):
    next=prev + current
    print(next)
    prev=current
    current=next
print(fibacacci(8))