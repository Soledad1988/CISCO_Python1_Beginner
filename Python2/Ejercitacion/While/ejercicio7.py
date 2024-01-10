#Escriba un programa que solicite una contraseña (El texto de la contarseña no es importante)
# y la vuelva a solicitar hasta que las dos contraseñas coincidan

print('CONFIRME SU CONTRASEÑA')

contraseña = input('Escriba su contarseña ')

repet_Contraseña = input('Escriba de nuevo su contraseña ')

while contraseña != repet_Contraseña:
    print('Intentelo de nuevo')

    contraseña = input('Escriba su contarseña ')
    repet_Contraseña = input('Escriba de nuevo su contraseña ')

print('Contraseña confirmada ')