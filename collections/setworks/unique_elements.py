st1={10,20,30,40,50}
st2={10,20,60,70,80}
st3=st1.intersection(st2)
st4=st1.union(st2)
st5=st1.difference(st2)
st1.remove(50)

users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]
rahul_follows=["rohit","kohli","rishab","rahul"]
sanju_followers=["sanju","rohit","kohli"]
sanju_foll=set(sanju_followers)
rahul_foll=set(rahul_follows)
users1=set(users)
suggest=users1.difference(rahul_foll)
# mutual_friends=rahul_foll.intersection(sanju_foll)
mutual_friends=set(rahul_follows).intersection(set(sanju_followers))
# print(mutual_friends)



