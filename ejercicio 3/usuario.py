class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña  
    
    def iniciar_sesion(self, usuario, clave):
        return usuario == self.nombre_usuario and clave == self.contraseña
    
    def cambiar_contraseña(self, nueva_contraseña):
        self.contraseña = nueva_contraseña
        return "Contraseña actualizada con éxito."

class Administrador(Usuario):
    def __init__(self, nombre_usuario, contraseña, permisos):
        super().__init__(nombre_usuario, contraseña)
        self.permisos = permisos
    
    def gestionar_usuarios(self):
        return f"El administrador {self.nombre_usuario} está gestionando usuarios con permisos: {self.permisos}."

class Cliente(Usuario):
    def __init__(self, nombre_usuario, contraseña):
        super().__init__(nombre_usuario, contraseña)
    
    def realizar_compra(self):
        return f"El cliente {self.nombre_usuario} ha realizado una compra."

admin = Administrador("admin123", "segura123", "Todos")
cliente = Cliente("josue Perez", "compra456")

print(admin.iniciar_sesion("admin123", "segura123"))  
print(cliente.iniciar_sesion("josue Perez", "claveIncorrecta"))  
print(admin.gestionar_usuarios())  
print(cliente.realizar_compra()) 
print(cliente.cambiar_contraseña("nuevaClave789"))  



