#Escriba un programa que pregunte una y otra vez si desea terminar el programa,
# salvo si se contesta S o s (en mayuscula o en minuscula)

print('Escriba S o s si desea finalizar')
x = input('Desea continuar con el programa? ')

while x!="S" and x!="s":
    x = input('Desea continuar con el programa? ')

print('Hasta la vista')