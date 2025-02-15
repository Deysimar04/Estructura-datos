 lista=[]
def agregar(numero):
lista.append(numero)
print (f"Numero {numero} agregado.")
def eliminar():
 if lista:
  eliminado = lista.pop()
  print (f"Numero {eliminado} eliminado.")
 else:
  
  print("la lista esta vacia no hay nada que eliminar")
  
while True:
   print("\nLista actual:", lista)
   print("opciones , elija una: ")
print(" 1.agregar un numero")
print("2.eliminar el ultimo numero")
print("3.Salir")
opcion = input("selecciona una opcion (1/2/3):")
 if opcion == "1":
 numero = int(input("ingrese un numero para agregar: "))
elif opcion == "2":
eliminar()
elif opcion == "3":
print(" ejecutando salida del programa....")

break


else: 

print("opcion no valida intente de nuevo")



