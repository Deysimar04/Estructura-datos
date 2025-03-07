class Electrodomestico:
    def __init__(self, marca, modelo, consumoEnergético):
        self.marca = marca
        self.modelo = modelo
        self.consumoEnergético = consumoEnergético
    
    def encender(self):
        return f"El {self.marca} {self.modelo} está encendido."

class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, consumoEnergético, capacidad):
        super().__init__(marca, modelo, consumoEnergético)
        self.capacidad = capacidad
    
    def encender(self):
        return f"La lavadora {self.marca} {self.modelo} ha iniciado el ciclo de lavado."

class Refrigerador(Electrodomestico):
    def __init__(self, marca, modelo, consumoEnergético, tieneCongelador):
        super().__init__(marca, modelo, consumoEnergético)
        self.tieneCongelador = tieneCongelador
    
    def encender(self):
        return f"El refrigerador {self.marca} {self.modelo} está regulando la temperatura."


lavadora = Lavadora("Whirlpool", "SupremeCare", "500W", "15kg")
refrigerador = Refrigerador("Bosch", "VitaFresh", "300W", True)

print(lavadora.encender())  
print(refrigerador.encender())  