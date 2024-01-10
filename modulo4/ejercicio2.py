#Triángulos y el Teorema de Pitágoras
#Observa el código en el editor. Le pide al usuario tres valores. 
#Después hace uso de la función is_a_triangle. El código esta listo para correrse.

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Ingresa la longitud del primer lado: '))
b = float(input('Ingresa la longitud del segundo lado: '))
c = float(input('Ingresa la longitud del tercer lado: '))

if is_a_triangle(a, b, c):
    print('Si, si puede ser un triángulo.')
else:
    print('No, no puede ser un triángulo.')


#En el segundo paso, intentaremos verificar si un triángulo es un triángulo rectángulo.

#Para ello haremos uso del Teorema de Pitágoras:

#c2 = a2 + b2

#¿Cómo saber cual de los tres lados es la hipotenusa?

#La hipotenusa es el lado más largo.

#Aquí esta el código:

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))

