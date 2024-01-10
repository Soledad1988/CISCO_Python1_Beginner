myStr = "Hello World"

dir(myStr)#que podeos hacer con un determinado tipo de dato

#print(dir(myStr))

print(myStr.upper()) #todo mayuscula
print(myStr.lower()) #todo a minuscula
print(myStr.swapcase())
print(myStr.capitalize())

myStr.raplace() #reemplazar
print(myStr.replace("hello", "Bye"))

print(myStr.count("0"))

print(myStr.startswith("Hola")) #empieza mi texto con Hola? false/true
print(myStr.endswith("world")) #como termina una palabra

print(myStr.split()) #separa el texto segun el caracter de espacio

print(myStr.split(',')) #separa segun la coma, tambien pueden ser caracteres

print(myStr.find('o')) #devuelve la posicion 

print(len(myStr)) #imprime la longitud

print(myStr.index('e')) #devuelve la posicion del indice

print(mySrt.isnumeric())
print(mySrt.isalpha())

#concatenar
myStr = "Brenda"
print("My name is "+ myStr)
print(f"My name is {myStr}")
print("My name is {0}".format(myStr))