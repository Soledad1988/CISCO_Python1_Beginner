# Escriba un programa que pregunte una y otra vez que si desea continuar con el programa.
# Siempre que se conteste sí (en minuscula y con tilde)}

print("DIGA sí PARA CONTINUAR")
x = input("¿Desea continuar el programa?: ")

while x == "sí":
    x = input("¿Desea continuar el programa?: ")

print("¡Hasta la vista!")