'''
Dado un rango de números enteros [a, b] (a <= b), tu tarea es escribir una función
suma_primos_en_rango que tome como argumentos dos números enteros a y b y devuelva la suma
de todos los números primos dentro del rango [a, b] (incluidos a y b si son primos).
'''

def suma_primos_en_rango(a, b):
    def es_primo(n):
        # si n es menor o igual a 1
        if n <= 1:
            return False
        # si n es menor o igual a 3
        if n <= 3:
            return True
        # comprueba si n es dibisible entre 2 o 3
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        # se ejecuta siempre que el cuadrado de i sea menor a  o igual n
        # permite dtener la busqueda de divisores primos de n una vaz que sellega a la raiz cuadrada de n
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            # se incrementa i en 6 para tomar el siguiente primo sin que sea multiplo de 2 o 3, los primos mayores que 3
            # siguen la formula 6k(+|-)1
            i += 6
        return True
    # variable utilizada para almacenar la suma de los numeros dentro del rango a,b
    suma = 0
    for num in range(a, b + 1):
        # comprueba si el número es primo
        if es_primo(num):
            suma += num
    return suma

# imprime el resultado
print(suma_primos_en_rango(2, 3))  

