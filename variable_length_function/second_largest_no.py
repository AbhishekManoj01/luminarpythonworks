def second_largest_no(*args):
    sorted_numbers=sorted(args,reverse=True)
    return sorted_numbers[1]


print(second_largest_no(10,30,20))
