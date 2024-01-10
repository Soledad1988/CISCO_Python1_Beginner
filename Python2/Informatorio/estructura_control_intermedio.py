#Nivel Intermedio

#Se necesita calcular el resultado final de un cuestionario realizado por una persona
#Solicita cantidad total de preguntas y luego cantidad de respuestas correctars
#Si el porcentaje de respuestas es >=90 resultado EXELENTE, >=70 BUENO
# >=60 APROBADO; <= 60 NO ALCANZO

preguntas = int(input('Ingrese total de preguntas: '))
print('Total de preguntas>>> ', preguntas)

correctas = int(input('Ingrese cantidad de respuestas correctas '))
print('Total de respuestas correctas >>> ', correctas)

porcentaje = correctas * 100 / preguntas
if (porcentaje >= 90):
    print('EXCELENTE')
elif (porcentaje >= 70):
    print('BUENO')
elif (porcentaje >= 60):
    print('APROBADO')
else:
    print('NO ALCANZO')




#Programa que solicite ingresen las ventas de 2 dias,
#y luego se informe por pantalla si se vendio mas el dia 1, el dia 2
# o si se vendio lo mismo en ambos dias