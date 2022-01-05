import math
f_list = [1,2,3,4,5,64,99,12,11,43,8,9]

def find_number(f_list, key):
    l = 0
    r = len(f_list) - 1
    while l <= r:
        mid_index = math.floor((l+r)/2)
        if f_list[mid_index] == key:
            return "number found"
        elif f_list[mid_index] > key:
            r = mid_index - 1
        else:
            l = mid_index + 1
    return "number not found"


print(find_number(f_list, 2))
