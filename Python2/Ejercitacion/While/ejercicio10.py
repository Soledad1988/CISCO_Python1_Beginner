# Escriba un programa que solicite una contraseña (El texto de la contraseña no es importante)
#y la vuelva a solicitar hasta que las dos coincidan, hasta un limite de tres peticiones

#No me sale
print('Confirme su Contraseña')

contraseña = input('Escriba su contarseña ')
print('Tiene 3 intentos para confirmar su contarseña ')

repet_Contraseña = input('Escriba de nuevo su contraseña ')

contador = 0

while contraseña != repet_Contraseña and contador < 4:
    print('Las contraseñas no coinciden. Intentelo de nuevo')
    repet_Contraseña = input('Escriba de nuevo su contraseña ')
    contador += 1

    if contraseña != repet_Contraseña:
        print('Su contraseña ha sido confirmada, hasta la vista')
    else:
        print('Lo siento no ha confirmado su contraseña, Hasta la vista')

