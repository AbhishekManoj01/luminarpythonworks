student_data={
    "hari": [45,40,35],
    "vipin":[34,40,45],
    "vijay":[45,40,35],
    "vinay":[50,50,50]
    }
# index=4
# for i,element in enumerate(student_data):
#     if i+1==index:
#         marks=student_data.get(element)
#         avg=sum(marks)/len(marks)
#         print(avg)


student_avg_mark={k:sum(v)/len(v) for k,v in student_data.items()}
print(student_avg_mark)