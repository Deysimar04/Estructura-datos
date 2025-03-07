class FiguraGeometrica:
    def calcularArea(self):
        pass

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        return (self.base * self.altura) / 2

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado
    
    def calcularArea(self):
        return self.lado ** 2


triangulo = Triangulo(10, 5)
cuadrado = Cuadrado(4)

print("Área del triángulo:", triangulo.calcularArea())  
print("Área del cuadrado:", cuadrado.calcularArea())  
