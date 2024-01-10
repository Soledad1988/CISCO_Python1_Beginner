#Escriba un programa que pida un numero par y a continuacion un numero impar
#En caso de que uno o los dos valores no sean correctos se mostrara
#uno o dos avisos

print("-"*120)
print("PAR E IMPAR")
print("-"*120)

par = int(input('Ingrese un numero par: '))
impar = int(input('Ingrese un numero impar: '))

if par%2==1:
    print('No ha escrito un número par')
    print('Ejecute de nuevo el programa')
    print('para volver a intentarlo')
else:
    if impar%2==0:
        print('No ha escrito un numero impar')
        print('Ejecute de nuevo el programa')
        print('para volver a intentarlo')
    else:
        print('¡Gracias por su colaboracio!')