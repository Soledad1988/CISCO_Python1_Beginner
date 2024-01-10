#¿Cómo utilizar un diccionario?
#Analiza el código en el editor:

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}


#El siguiente código busca de manera segura palabras en francés:


dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")