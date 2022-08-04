"""
    1.- lopp through each element of the list
    2.- Each element of list is sorting if it has a larger element to his left
    3.- If true = Interchange

"""


list = [5,10,3,12,10,6]

for i in range(1,len(list)):
    aux = list[i]
    j = i -1
    while j >= 0 and aux < list[j]:
        list[j+1] = list[j]
        list[j] = aux 
        j -= 1

print(list)