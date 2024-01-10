#Ejercici 1: Escriba un programa que pida primero un número par y luego un número impar
#En caso de que uno o los dos valores no sean correctos, se mostrara un unico aviso:


print('-'*100)
print('Par e Impar\n')
print('-'*100)

par = int(input('Ingrese un número par: '))
impar = int(input('Ingrese un número impar: '))

if (par%2 == 1 or impar%2 ==0):
    print('Uno o mas de los valores que ha escrito no son correctos')
    print('Ejecute de nuevo el programa para volver a intentarlo')   
else:
     print('¡Gracias por su colaboracio!')