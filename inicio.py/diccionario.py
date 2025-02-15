persona = dict()

while True:
    print("selecione una opcion ")
    print ("agregar clave valor ")
    print ("eliminar clave ")
    print("salir.")
    opcion =int(input())
    if opcion==1:
        clave= input("Ingrese el nombre: ")
        valor=input("ingrese valor")
        persona.update({clave:valor})
    if opcion ==2:
        clave= input("Ingrese el nombre a eliminar: ")
        persona.pop(clave)
    if opcion==3:
        break
    print(persona)
    


"""

persona["nombre"] = input("Ingrese el nombre: ")
persona["valor"] = int(input("Ingrese el valor : "))


persona["clave"] = input("Ingrese la clave: ")


print("\nInformación de la persona:")
for clave, valor in persona.items():
    print(f"{clave.capitalize()}: {valor}")


clave_actualizar = input("\n¿Qué dato desea actualizar? (nombre, apellido, clave): ").lower()

if clave_actualizar in persona:
    nuevo_valor = input(f"Ingrese el nuevo valor para {clave_actualizar}: ")
    persona[clave_actualizar] = int(nuevo_valor) if clave_actualizar == "edad" else nuevo_valor
    print("\nDatos actualizados correctamente.")
else:
    print("El dato ingresado no es válido.")


print("\nInformación actualizada de la persona:")
for clave, valor in persona.items():
    print(f"{clave.capitalize()}: {valor}")
    """
