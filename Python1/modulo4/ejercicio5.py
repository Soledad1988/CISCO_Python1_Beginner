#Recursividad
#Existe algo más que se desea mostrar: es la recursividad.

#Este termino puede describir muchos conceptos distintos, pero uno de ellos, 
#hace referencia a la programación computacional.

#Aquí, la recursividad es una técnica donde una función se invoca a si misma.

#Tanto el factorial como la serie Fibonacci, son las mejores opciones 
#para ilustrar este fenómeno.

#La serie de Fibonacci es un claro ejemplo de recursividad. 
#Ya te dijimos que:

#Fibi = Fibi-1 + Fibi-2

#El número i se refiere al número i-1, y así sucesivamente hasta llegar a 
#los primeros dos.

#¿Puede ser empleado en el código? Por supuesto que puede. 
#Puede hacer el código más corto y claro.

#La segunda versión de la función fib() hace uso directo de la recursividad:

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)



def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)


def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):
    print(n, "->", fib(n))
