# Ejercicio 1: Factorial de un número

def factorial(n):
    if n ==0 or n==1 :
        return 1
    else:
        return n*(factorial(n-1))
print(factorial(n=5))