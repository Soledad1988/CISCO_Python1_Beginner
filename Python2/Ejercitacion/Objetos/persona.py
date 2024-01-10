#Definir la clase persona con sus metodos y atributos

class Persona:
    def __int__(self, nombre, edad, genero, estatura, peso):
        self.nombre = nombre
        self.edad= edad
        self.genero = genero
        self.estatura = estatura
        self.peso = peso

        def hablar(self):
            print("Hola soy {}".format(self.nombre))
        
        def correr(self):
            print("{} esta corriendo".format(self.nombre))
        
        def caminar(delf):
            print("{} esta caminando".format(self.nombre))


persona1 = Persona("Juan", 23, "Masculino", 170, 90)
persona2 = Persona("Maria", 25, "Femenino", 160, 70)

print(persona1.nombre)
print(persona1.edad)
print(persona1.sexo)
print(persona1.estatura)
print(persona1.peso)
persona1.hablar()
persona1.correr()
persona1.caminar()