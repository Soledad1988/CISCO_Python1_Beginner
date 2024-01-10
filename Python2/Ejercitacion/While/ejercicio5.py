#Escriba un programa que pregunte una y otra vez si desea continuar con el programa, 
# siempre que se conteste S O s (en mayuscula o in minuscula)

print('Diga S o s para continuar el programa')
x = input('Desea continuar con el programa? ')

while x=="S" or x=="s":
    x = input('Desea continuar con el programa? ')

print('Hasta la vista')