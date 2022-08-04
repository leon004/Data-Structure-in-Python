list = [4,2,6,8,5,7]

for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            aux = list[j]
            list[j] = list[j+1]
            list[j+1] = aux
            print(list)
