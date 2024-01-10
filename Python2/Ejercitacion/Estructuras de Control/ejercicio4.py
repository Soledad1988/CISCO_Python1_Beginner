#Escriba un programa que pida primero un numero par y a continuacion
#un numero impar. En cada peticion, si el valor no es correcto se mostrara un aviso

print("-"*120)
print("PAR E IMPAR")
print("-"*120)

par = int(input('Ingrese un numero par: '))
if par%2==1:
    print('No ha escrito un numero par')
    print('Ejecute de nuevo el programa')
    print('para volver a intentarlo')
    impar =int(input('Ingrese un numero impar: '))
    print('Ejecute de nuevo el programa')
    print('para volver a intentarlo')
else:
    impar =int(input('Ingrese un numero impar: '))
    if(impar%2==0):
        print('No ha ingresp un numero impar')
        print('Ejecute de nuevo el programa')
        print('para volver a intentarlo')
    else:
        print('¡Gracias por su colaboracion!')
