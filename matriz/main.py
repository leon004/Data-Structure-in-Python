from os import system



"""
MATRIZ  5*5
        Columnas
       0 1 2 3 4 5 |
    0| 1 2 3 4 5 6 |
    1| 8 1 2 8 9 5 |
    2| 9 7 8 5 4 2 |
    3| 4 5 6 2 1 5 |
    4| 5 4 6 2 0 3 |
"""

#matriz = [[1,2,3,4,5,6], [8,1,2,8,9,5], [9,7,8,5,4,2], [4,5,6,2,1,5], [5,4,6,2,0,3]]

#Creacion de una matriz con compresion de listas

matriz = [list(range(10)) for x in range(10)]

for x in matriz:
    print(x)
