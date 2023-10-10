#Variables

var = 1
print(var)

#Como emplear una variable
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)


#Se puede utilizar print() para combinar texto con variables utilizando
#  el operador + para mostrar cadenas con variables, por ejemplo:
var = "3.8.5"
print("Python version: " + var)

#Resolviendo problemas matemáticos simples
#Ahora deberías poder construir un programa corto que resuelva problemas matemáticos simples 
#como el teorema de Pitágoras:
#El cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos.
#El siguiente código evalúa la longitud de la hipotenusa 
#(es decir, el lado más largo de un triángulo rectángulo, el opuesto al ángulo recto) 
#usando el teorema de Pitágoras:
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)