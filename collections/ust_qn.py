arr=[100,800,300,600,500,400,700,200]
odd_postion_ele=[arr[i] for i in range(0,len(arr)) if i%2!=0]
 #odd_postion_number=[num for index,num in enumerate(arr) if index%2!=0]
print(odd_postion_ele)

odd_postion_ele.reverse()
print(odd_postion_ele)