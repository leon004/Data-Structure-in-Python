"""
Recursividad: Es una funcion que se llama a si misma
Ejemplo -> factorial de 4! = 4 * 3 * 2 * 1 = 24
"""

def factorial(n):
    if n == 1:
        return 1
    else: 
        return n * factorial(n-1)

"""
Ejemplo
n = 4 
return 4 * factorial(3)

n = 3
return 3 * factorial(2)

n = 2 
return 2 * factorial(1)

n = 1
return 1

"""

print(factorial(4))