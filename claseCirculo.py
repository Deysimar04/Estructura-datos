class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.1416 * self.radio ** 2
    
    def circunferencia(self):
        return 2 * 3.1416 * self.radio


c = Circulo(2)
print("Área:", c.area())
print("Circunferencia:", c.circunferencia())

