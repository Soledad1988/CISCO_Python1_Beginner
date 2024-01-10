#Escriba un programa que pida dos numeros enteros y que calcule su division
#escribiendo si la division es exacta o no //  si puede mejorarlo trate que no se pueda
#dividir por cero

print("-"*120)
print('DIVISOR DE UN NUMERO')
print("-"*120)

dividendo = int(input('Ingrese un numero: '))
divisor = int(input('Ingrese otro numero: '))

if divisor == 0:
        print('no se puede dividir por cero')
else:
    if dividendo % divisor == 0:
        print(f'La division es exacta, cociente: {dividendo // divisor}')
    else:
        print(f'La division no es exacta, cociente: {dividendo // divisor}')
        print(f'Resto:  {dividendo % divisor}')