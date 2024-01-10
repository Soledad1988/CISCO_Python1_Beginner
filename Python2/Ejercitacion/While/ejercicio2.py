# Escriba un programa que pregunte una y otra vez si desea terminar el programa,
# salvo si se contesta exactamente SI (en mayuscula y sin tilde)

print('Diga SI para finalizar')
x = input('¿Desea terminar el progarma?')

while x != "SI":
    x = input('¿Desea terminar el progarma?')

print('Hasta la vista')
