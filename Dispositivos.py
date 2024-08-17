class Dispositivo(): #Este codigo lo  hice de manera un poco diferente para probar cosas nuevas.
    def __init__(self, tipo, modelo, procesador, memoria, almacenamiento, compra):
        # Inicializa los atributos del dispositivo
        self.tipo = tipo                    
        self.modelo = modelo                
        self.procesador = procesador        
        self.memoria = memoria              
        self.almacenamiento = almacenamiento 
        self.compra = compra 
        #Atributos privados 
        self.__marca = "PHR"       
        self.__origen = "Importado"           
        self.__venta = round(compra * 1.7, 2)
    
    #Devuelve la marca del dispositivo
    def get_marca(self):
        return self.__marca
    #Devuelve el origen del dispositivo
    def get_ori(self):
        return self.__origen
    #Devuelve precio de venta del dispositivo
    def get_venta(self):
        return self.__venta

    def MostrarDispositivos(self):
        #Muestra la informacion del dispositivo
        print(f"Dispositivo {self.tipo} - Modelo: {self.modelo}")
        print(f"Procesador: {self.procesador}, Memoria RAM: {self.memoria} GB")
        print(f"Almacenamiento: {self.almacenamiento} GB, Marca del dispositvio: {self.__marca}")
        print(f"Precio de compra: ${self.compra}")
        print(f"Precio de Venta: ${self.__venta}")
        print(f"\n-------------------------------------------------------------\n")

#Almacenar informacion del usuario para crear un objteo de la clase Dispositivo
almacenar = [Dispositivo(input("Tipo de dispositivo (celular/tablet/laptop):"), input("Modelo: "), input("Procesador: "), 
                         int(input("Memoria RAM (en GB): ")), int(input("Almacenamiento (en GB): ")), float(input("Precio Compra: $")))
                         for _ in range(1)]
print("\n---------------------------------------------------------------\n")

#Muestra la infromacion de cada dispositivo
for dispositivo in almacenar: dispositivo.MostrarDispositivos()
