list = [4,2,6,8,5,7,0]

for i in range(len(list)):
    min = i
    for x in range(i, len(list)):
        if list[x] < list[min]:
            min = x
    aux = list[i]
    list[i] = list[min]
    list[min] = aux

print(list)
