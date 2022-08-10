from lista import ListaDoblementeEnlazada

def montone():

    for i in range(1,9999999999):
        if i % 13563 == 0 and i != 13563:
            i = str(i)
            if( i == i[::-1]):
                return True
            

montone()