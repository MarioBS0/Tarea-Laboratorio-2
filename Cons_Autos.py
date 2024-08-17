class Auto:
    def __init__(self, marca, modelo, año, tipoMotor, color, puertas, transmision, precioCompra, tipoAuto):
        self.marca = marca 
        self.modelo = modelo 
        self.año = año                   
        self.tipoMotor = tipoMotor      
        self.color = color                
        self.puertas = puertas            
        self.transmision = transmision    
        self.precioCompra = precioCompra  
        self.tipoAuto = tipoAuto        
        self.precioVenta = round(precioCompra * 1.40, 2)  #Redonde a 2 digitos decimales

    def mostrarAuto(self):
        # Muestra la información del auto
        print(f"Auto {self.marca} {self.modelo} ({self.año})")
        print(f"Motor: {self.tipoMtor}, Color: {self.color}, Puertas: {self.puertas}")
        print(f"Tipo: {self.tipoAuto}, Precio Compra: {self.precioCompra}")
        print(f"Precio Venta: {self.precioVenta} COP\n")

# Lista para almacenar los autos registrados
concesionario = []

# Función para registrar un auto
def registrarAuto():
    marca = input("Marca del auto: ")
    modelo = input("Modelo del auto: ")
    año = int(input("Año del auto: "))
    tipoMotor = input("Tipo de motor(Gasolina/Diesel): ")
    color = input("Color del auto: ")
    puertas = int(input("Número de puertas: "))
    transmision = input("Tipo de transmisión (manual/automática): ")
    precioCompra = float(input("Precio de compra: "))
    tipoAuto = input("Tipo de auto (Nacional/Importado): ")
    print("---------------------------------------------------")
    
    auto = Auto(marca, modelo, año, tipoMotor, color, puertas, transmision, precioCompra, tipoAuto)
    concesionario.append(auto)
    print(f"Auto {auto.marca} {auto.modelo} registrado.\n")

# Función para mostrar la información de todos los autos
def mostrarAutos():
    for auto in concesionario:
        auto.mostrarAuto()

# Registrar autos y mostrar la lista
registrarAuto()
registrarAuto()
print("\nAutos registrados:\n")
mostrarAutos()
