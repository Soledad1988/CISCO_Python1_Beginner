a=input('Ingrese la edad de la persona: ')
a=int(a)
print(a)

if (a>18):
    print('Persona mayor de edad')
else:
    print('Persona menor de edad')

#Desarrollar un programa que solicite la cantidad de intentos fallidos
#de ingreso de una contraseña, si la cantidad es > 5 veces, debe informar "Cuenta bloqueada"

#Condicional Alternativo if...else
edad=int(input('Cuantos años tienes? '))
if (edad < 18):
    print('Es menor de edad')
else:
    print('Es mayor de edad')