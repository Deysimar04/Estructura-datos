class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def get_cantidad_disponible(self):
        return self.cantidad_disponible

    def set_cantidad_disponible(self, cantidad_disponible):
        self.cantidad_disponible = cantidad_disponible

    def calcular_total(self, cantidad):
        return self.precio * cantidad


producto = Producto("iphone 13 ", 5000, 5)
cantidad_comprada = 5
print(f"Total por {cantidad_comprada} {producto.get_nombre()}s: ${producto.calcular_total(cantidad_comprada)}")
