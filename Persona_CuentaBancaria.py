class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    
    def presentarse(self):
        print(f"Mi nombre es {self.nombre}, tengo {self.edad} años y mi género es {self.genero}.")

class CuentaBancaria:
    def __init__(self, titular, numero_de_cuenta, saldo=0.0):
        self.titular = titular  
        self.numero_de_cuenta = numero_de_cuenta
        self.saldo = saldo
    
    def modificar_saldo(self, monto):
        if self.saldo + monto >= 0:
            self.saldo += monto
            print(f"Transacción exitosa. Nuevo saldo: {self.saldo:.2f}")
        else:
            print("Fondos insuficientes para realizar la transacción.")
    
    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo:.2f}")

persona1 = Persona("Deysimar", 18, "Femenino")
persona1.presentarse()  


cuenta1 = CuentaBancaria(persona1, "123456789", 1000.0)


cuenta1.consultar_saldo()
cuenta1.modificar_saldo(500)  
cuenta1.modificar_saldo(-300)  
cuenta1.modificar_saldo(-1500)  

