class Vehiculo:

    marca: str
    modelo:int
    color:str
    cilindraje: int
    numeroRuedas: int
    combustible: int
    
    
    def __init__(self, marca:str, combustible:int)-> None:
        self.marca = marca
        self.combustible = combustible
    
    def __str__(self)-> str:
        return f"Tipo de vehículo: {self.tipo}. Marca: {self.marca}. Nivel de combustible: {self.combustible}."

    def encender(self):
        pass

    def acelerar(self):
        pass

    def frenar(self):
        pass

    def apagar(self):
        pass

class Moto(Vehiculo):
     pass

class Carro(Vehiculo):
    pass

vehiculo1 = Vehiculo('mazda',80)
print(vehiculo1)

moto1 = Moto('honda',70)
print(moto1)

carro1 = Carro('renaul',80)
print(carro1)






        

