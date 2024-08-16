class Perro():
    def __init__(self, nombre, edad, raza, peso, genero, pelaje, color, ojos):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso
        self.genero = genero
        self.pelaje = pelaje
        self.color = color
        self.ojos = ojos
        self.estado = "NO ATENDIDO"
        self.clasificacion = "Perro Grande" if peso >= 10 else "Perro Pequeño"

    def atender(self):
        self.estado = "ATENDIDO"

    def mostrarInformacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Raza: {self.raza}")
        print(f"Peso: {self.peso} kg")
        print(f"Genero: {self.genero}")
        print(f"Tipo Pelaje: {self.pelaje}")
        print(f"Color del Pelaje: {self.color}")
        print(f"Color de Ojos: {self.color}")
        print(f"Estado: {self.estado}")
        print(f"Clasificación: {self.clasificacion}")
        print("-------------------------")

# Crear la lista para almacenar los perros
veterinaria = []

# Función para registrar un perro
def registrarPerro():
    nombre = input("Ingrese el nombre del perro: ")
    edad = int(input("Ingrese la edad del perro (en años): "))
    raza = input("Ingrese la raza del perro: ")
    peso = int(input("Ingrese el peso del perro (en kg): "))
    genero = input("Genero (Macho/Hembra): ")
    pelaje = input("Pelaje(Lago, Corto, Rizado, Sin Pelo): ")
    color = input("Color de pelaje: ")
    ojos = input("Color de ojos: ")
    print("---------------------------------------------------")
    
    perro = Perro(nombre, edad, raza, peso, genero, pelaje, color, ojos)
    veterinaria.append(perro)
    
    perro.atender()
    print(f"{perro.nombre} ha sido registrado y su estado ha cambiado a 'ATENDIDO'.\n")

# Función para mostrar la información de todos los perros
def mostrarPerros():
    for perro in veterinaria:
        perro.mostrarInformacion()

# Registro de perros
cantidad_perros = int(input("¿Cuántos perros desea registrar? "))
for _ in range(cantidad_perros):
    registrarPerro()

# Mostrar la información de todos los perros registrados
print("\nInformación de los perros registrados:")
mostrarPerros()
