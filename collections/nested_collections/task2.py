student_data={
    "hari":[45,40,35],
    "vipin":[34,40,45],
    "vinay":[45,40,35],
    "bijoy":[33,40,35],
    "anvin":[50,50,50]
}


# for i,element in enumerate(student_data):
#     if i+1==index:
#         print(i,element)
#         marks=student_data.get(element)
#         avg=sum(marks)/len(marks)
#         print(f"")
# for i,element in enumerate(student_data):
#         marks=student_data.get(element)
#         student_name_avg={element:sum(marks)/len(marks)}
#         print(student_name_avg)
student_avgs={k:round(sum(v)/len(v)) for k,v in student_data.items()}
print(student_avgs)


so
