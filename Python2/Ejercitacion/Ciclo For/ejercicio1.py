#Escriba un programa que pida dos numeros enteros y que escriba que numeros
#son pares y cuales impares desde el primero hasta el segundo
#Ayuda: un numero es par cuando el resto de su division entre dos es cero
#(NUMERO%2==0) e impar ciando no lo es

print('Pares e Impares')

num1 = int(input('Ingrese un numero entero '))
num2 = int(input(f'Escriba un numero estero mayor o igual que {num1} '))

if num2 < num1:
    print(f'Le he pedido un numero entero mayor o igual a {num1} ')
    #num2 = int(input(f'Escriba un numero estero mayor o igual que {num1} '))
else:
    for x in range(num1, num2+1):
        if x%2 == 0:
             print(f'El numero {x} es par')
        else:
            print(f'El numero {x} es impar')
