#La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre del barrio
# y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)

#La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra 
#anterior a M y los barrios no céntricos con nombre posterior a la M, y la sección B el resto.

#Debemos hacer un programa que dado el nombre del barrio y la ubicación, 
# nos informe en que sección se encuentra.

print('Secciones para recoleccion')

seccion = input('Ingrese el nombre del Barrio ')

if seccion >= range("A","M"):
    print('Secciones A, Barrio Centrico')
elif seccion < range("M"):
    print('Seccion A, Barrio No centrico')
else:
    print('Seccion B')