class Vehiculo:
    CAPACIDAD_MAXIMA_COMBUSTIBLE = 100  
    CONSUMO_POR_KM = 2  

    def __init__(self, marca: str, combustible: int, tipo: str) -> None:
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo
        self.encendido = False  

    def __str__(self) -> str:
        return f"Tipo de vehículo: {self.tipo}. Marca: {self.marca}. Nivel de combustible: {self.combustible} galones."

    def encender(self):
        """Método para encender el vehículo verificando el nivel de combustible."""
        if self.combustible < (0.1 * self.CAPACIDAD_MAXIMA_COMBUSTIBLE):
            print(f"Advertencia: {self.tipo} {self.marca} tiene poco combustible. ¡Ve a la gasolinera Rapidooo!")
        else:
            self.encendido = True
            print(f"{self.tipo} {self.marca} encendido con éxito.")

    def apagar(self):
        """Apaga el vehículo."""
        if self.encendido:
            self.encendido = False
            print(f"{self.tipo} {self.marca} apagado.")
        else:
            print(f"{self.tipo} {self.marca} ya está apagado.")

    def avanzar(self, distancia: int):
        """
        Método para hacer avanzar el vehículo una cantidad de kilómetros.
        Cada kilómetro consumirá combustible. Si el combustible se acaba, el vehículo se detendrá.
        """
        if not self.encendido:
            print(f"No puedes avanzar. {self.tipo} {self.marca} está apagado.")
            return

        consumo_total = distancia * self.CONSUMO_POR_KM

        if consumo_total > self.combustible:
            print(f"El {self.tipo} {self.marca} se quedó sin combustible y se ha detenido.")
            self.combustible = 0
            self.apagar()
        else:
            self.combustible -= consumo_total
            print(f"El {self.tipo} {self.marca} ha avanzado {distancia} km. Combustible restante: {self.combustible} galones.")

           
            if self.combustible < (0.1 * self.CAPACIDAD_MAXIMA_COMBUSTIBLE):
                print(f"Advertencia: {self.tipo} {self.marca} tiene poco combustible. ¡Ve a la gasolinera!")

class Moto(Vehiculo):
    def __init__(self, marca: str, combustible: int) -> None:
        super().__init__(marca, combustible, "Moto")

class Carro(Vehiculo):
    def __init__(self, marca: str, combustible: int) -> None:
        super().__init__(marca, combustible, "Carro")

moto1 = Moto("Honda", 20) 
carro1 = Carro("Renault", 10) 

print(moto1)
moto1.encender()
moto1.avanzar(5)  

print(carro1)
carro1.encender()
carro1.avanzar(6)  