#Escriba un programa que pida dos numeros y que conteste
#cual es el menor y cual es el mayor o que escriba que son iguales

print('-'*120)
print('COMPARADOR DE NUMEROS')
print('-'*120)

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese otro numero: '))

if num1 > num2:
    print(f'mayor: {num1}, menor: {num2}')
else:
    if num1 < num2:
       print(f'mayor: {num2}, menor: {num1}') 
    else:
        print('Ambos numeros son iguales')