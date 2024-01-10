# Un local vende remeras por mayor y menor
# si la compra es por una cantidad mayor o igual a 10 remeras
# el precio por unidad es de tan solo el 80%

# Preguntar cuantas unidades de remeras se incluye en la compra y el precio por unidad
# devolver el precio total de la compra

precio = float(input('Ingrese precio por unidad: '))
unidades = int(input('Ingrese unidades: '))

if (unidades >= 10):
    total=unidades * precio * 0.8
else:
    total = unidades * precio

print('El total de la compra es: ',total)