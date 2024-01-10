# Escriba un programa que pregunte una y otra vez si desea terminar el programa,
# siempre y cuando que se conteste exactamente N (en mayuscula)

print('Presione N para continuar el programa')
x = input('¿Desea terminar el programa?')

while x == "N":
    x = input('Presione N para continuar el programa')

print('!Hasta la vista!')