#Escriba un programa que pida un numero par y si el valor no es correcto
#muestre un aviso. Si el valor es correcto, pedira un numero impar, si el valor
#no es correcto mostrara el mismo aviso

print("-"*120)
print("PAR E IMPAR")
print("-"*120)

par = int(input('Ingrese un numero par: '))

if(par%2==1):
    print('No ha escrito un número par')
    print('Ejecute de nuevo el programa para volver a intentarlo')
else:
    impar = int(input('Ingrese un número impar: '))
    if (impar%2==0):
         print('No ha escrito un número par')
         print('Ejecute de nuevo el programa para volver a intentarlo')
    else:
         print('¡Gracias por su colaboracion!')
