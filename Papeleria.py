class Cuaderno:
    def __init__(self, tipoHojas, precioCompra):
        self.tipoHojas = tipoHojas        
        self.precioCompra = precioCompra 
        self.__marca = "HOJITAS"              
        self.venta = round(precioCompra * 1.30 , 2) #Para redondear a 2 decimales 

    def get_marca(self):
        return self.__marca

    def mostrarInformacion(self):
        print(f"Cuaderno - Hojas: {self.tipoHojas}\n Marca: {self.__marca}\n Precio Venta: {self.venta}\n")

class Lapiz:
    def __init__(self, tipo, precioCompra):
        self.tipo = tipo                    
        self.precio_compra = precioCompra 
        self.__marca = "RAYAS"               
        self.venta = round(precioCompra * 1.30, 2)  #Para redondear a 2 decimales

    def get_marca(self):
        return self.__marca

    def mostrarInformacion(self):
        print(f"Lápiz - Tipo: {self.tipo}\n Marca: {self.__marca}\n Precio Venta: {self.venta}\n")

# Lista para almacenar los artículos registrados
papeleria = []

# Registra un cuaderno en la lista
def registrarCuaderno():
    tipoHojas = input("Cuaderno (50 hojas/100 hojas): ")
    precioCompra = float(input("Precio de compra: "))
    papeleria.append(Cuaderno(tipoHojas, precioCompra))
    print("Cuaderno registrado.")
    print("\n-----------------------------------------\n")

# Registra un lápiz en la lista
def registrarLapiz():
    tipo = input("Lapiz (grafito/colores): ")
    precioCompra = float(input("Precio de compra: "))
    papeleria.append(Lapiz(tipo, precioCompra))
    print("Lapiz registrado.")
    print("----------------------------------------------")

# Muestra la información de todos los artículos
def mostrarArticulos():
    for articulo in papeleria:
        articulo.mostrarInformacion()

# Registrar artículos y mostrar la lista
registrarCuaderno()
registrarLapiz()
print("\nArtículos registrados:\n")
mostrarArticulos()
