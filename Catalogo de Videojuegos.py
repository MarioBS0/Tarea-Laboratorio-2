class Videojuego:
    def __init__(self, titulo, plataforma, genero, modos_juego, desarrollador, fecha_lanzamiento, calificacion):
        # Inicializa los atributos del videojuego
        self.titulo = titulo 
        self.plataforma = plataforma  # Consola o sistema en el que está disponible
        self.genero = genero  # Clasificación del juego (acción, aventura, etc.)
        self.modos_juego = modos_juego  # Modos de juego disponibles (un jugador, multijugador, etc.)
        self.desarrollador = desarrollador  # Estudio o compañía que desarrolló el juego
        self.fecha_lanzamiento = fecha_lanzamiento  # Fecha en la que el juego fue lanzado
        self.calificacion = calificacion  # Calificación del juego por parte de críticos o usuarios
        self.__precio = 60  # Precio de venta del juego
    
    #Devuelve el precio del dispositivo
    def get_pre(self): 
        return self.__precio

    def mostrar_info(self):
        # Devuelve una cadena con la información del videojuego
        print(f"Título: {self.titulo}\n"
             f"Plataforma: {self.plataforma}\n"
             f"Género: {self.genero}\n"
             f"Modos de Juego: {self.modos_juego}\n"
             f"Desarrollador: {self.desarrollador}\n"
             f"Fecha de Lanzamiento: {self.fecha_lanzamiento}\n"
             f"Calificación: {self.calificacion}\n"
             f"Precio: ${self.__precio}\n")

# Solicita al usuario que ingrese la información del videojuego
almacenar = [Videojuego(
    input("Título del videojuego: "),  # Nombre del juego
    input("Plataforma: "),  # Plataforma (ej. Nintendo Switch, PlayStation, Xbox)
    input("Género: "),  # Género del juego (ej. Aventura, Acción, RPG)
    input("Modo de juego (Historia/Online): "),  # Modos de juego disponibles (ej. Un jugador, Multijugador)
    input("Desarrollador: "),  # Desarrollador del juego
    input("Fecha de lanzamiento: "),  # Fecha de lanzamiento
    input("Calificación: "),  # Calificación del juego (ej. 9/10, 10/10)
) for _ in range(1)]  # Ajusta el rango para añadir más juegos si lo deseas

print("\n---------------------------------------------------------------\n")

# Muestra la información de cada videojuego almacenado
for videojuego in almacenar:
    print(videojuego.mostrar_info())

