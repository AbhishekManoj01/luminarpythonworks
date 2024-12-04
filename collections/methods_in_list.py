# append  syn:def(self)
colours=["green","red","yellow"]
colours.append("yellow")
print(colours)

# pop  syn:def pop(self,index)
colours=["green","red","yellow"]
colours.pop()#colours.pop(1)
print(colours)

#insert syn:index(self,index,object)
colours=["green","red","yellow"]
colours.insert(0,"purple")
print(colours)
 
arr=[100,200,300,400,500]
k=int(input("enter the k value"))
for i in range(1,k+1):
    popeed_element=arr.pop()
    arr.insert(0,popeed_element)
print(arr)
    
#index syn:index(self,object)
colours=["green","red","yellow"]
red_index=colours.index("red")
print(red_index)

#copy syn:copy(self)
colour1=["green","red","yellow","white"]
colour2=colour1.copy()
colour2.pop()
print(colour2)
print(colour1)

#sort syn:sort()
lst=[3,4,2,5,6,7]
lst1=[3,4,2,5,6,7]
lst.sort() 
lst1.sort(reverse=True)
print(lst)
print(lst1)