#Condicionales if - if/else

#if true_or_false_condition:
#    perform_if_condition_true
#else:
#    perform_if_condition_false

#Ejemplo 1:
#Comenzaremos con el caso más simple - ¿cómo identificar el mayor de los dos números?:

# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
 
# Elige el número más grande
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
# Imprime el resultado
print("El número más grande es:", larger_number)

#Ejemplo 2:
#Ahora vamos a mostrarte un hecho intrigante. 
#Python tiene una característica interesante - mira el código a continuación:
# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
 
# Elige el número más grande
if number1 > number2: larger_number = number1
else: larger_number = number2
 
# Imprime el resultado
print("El número más grande es:", larger_number)
#se escribe la condicion en una sola linea, aunque suele ser confuso

#Ejemplo 3:
#Es hora de complicar el código - encontremos el mayor de los tres números. ¿Se ampliará el código? Un poco.
#Suponemos que el primer valor es el más grande. Luego verificamos esta hipótesis con los dos valores restantes.
#Observa el siguiente código:

# Se leen tres números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))
 
# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
largest_number = number1
 
# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number2 > largest_number:
    largest_number = number2
 
# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number3 > largest_number:
    largest_number = number3
 
# Imprime el resultado.
print("El número más grande es:", largest_number)
 