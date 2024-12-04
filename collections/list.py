colour=["red","pink","blue","red"]
print(colour)

for col in colour:
    print(col)

   #sum
# expence=[1000,1200,1300,1400]
# total=0
# for exp in expence:
#     total=total+exp
# print(total)


expence=[1000,5,1200,1300,1400,600]
max=expence[0]
min=expence[0]
for exp in expence:
    if exp>=max:
        max=exp
    if exp<min:
        min=exp
print(f"minimum number is {max}")
print(min)