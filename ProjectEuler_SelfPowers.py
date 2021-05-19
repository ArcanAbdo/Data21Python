
Range_list = list(range(1, 1001, 1))
new_list = []

for i in Range_list:
    new_list.append(i ** i)
    print(i)
    print(sum(new_list))

