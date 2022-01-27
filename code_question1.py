s = 1234
# output = [1234, 11223344, 111222333444, 111122223333444]


s_str = str(s)

output = []
count = 1

while count <= len(s_str):
    t = ''
    for i in s_str:
        t += i*count
    count += 1
    output.append(t)
print(output)
