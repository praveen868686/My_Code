# S = 'aaaabbbb'
# return 1
#
# S = 'eeee'
# return 0
#
S = 'example'
# return 4

# S = 'tddshdsjfkfdkfk'


def Solution(S):
    bet = list(set(S))
    print(bet)
    new_list = []
    for i in range(len(bet)):
        at = S.count(bet[i])
        new_list.append(at)
        i += 1
    print(new_list)

    count = 0
    for i in range(len(new_list)-1):
        list_traverse = True
        if len(new_list) > 1:
            z = i+1
            while list_traverse:
                if new_list[i] == new_list[z]:
                    count += 1
                    list_traverse = False
                    # break
                z += 1
                if z == len(new_list):
                    break
    return count

print(Solution(S))
