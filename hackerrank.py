# problem 1: Sales by Match

def sockMerchant(n, ar):
    list_set=set(ar)
    count = 0
    new_list = []
    for i in list_set:
        if ar.count(i)>1:
            new_list.append(ar.count(i))

    for u in new_list:
        count += u//2
    return count


ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(9,ar))
