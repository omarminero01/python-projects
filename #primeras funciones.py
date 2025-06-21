def devolver_distintos(a, b, c):
    suma = a + b + c
    lista = [a, b, c]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:  # suma entre 10 y 15 (incluidos)
        lista.sort()
        return lista[1]


print
'''Crea una función lamada devolver_distintos() que reciba 3
 integers como parámetros. 
Si la suma de los 3 numeros es mayor a 15, va a devolver el
 número mayor.
 Si la suma de los 3 numeros es menor a 10, va a devolver el
 número menor.
 Si la suma de los 3 números es un valor entre 10 y 15
 (incluidos) va a devolver el número de valor intermedio.'''