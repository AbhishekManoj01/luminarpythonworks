def poll(age):
    assert age>18,"invalid age"
    print("voted")
try:
   poll(14)
except Exception as e:
    print(e)