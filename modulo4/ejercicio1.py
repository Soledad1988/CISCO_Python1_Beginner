#Definamos una función que calcula el Índice de Masa Corporal (IMC).

#Como puedes observar, la formula ocupa dos valores:

#peso (originalmente en kilogramos)
#altura (originalmente en metros)
#La nueva función tendrá dos parámetros. Su nombre será bmi, pero si prefieres utilizar otro nombre, adelante.

def bmi(weight, height):
    return weight / height ** 2


print(bmi(52.5, 1.65))


#Calcular el IMC y convertir unidades del Sistema Inglés al Sistema Métrico
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))