num1 = 13423546546

list1= [int(i) for i in str(num1)]

new_list = []

while len(list1) != 0:
    max = list1[0]
    for i in list1:
        if i > max:
            max = i

    new_list.append(max)
    list1.remove(max)

print(new_list)
