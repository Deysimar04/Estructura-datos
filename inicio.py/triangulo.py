def triangulo_numeros(limite):
    for i in range(1, limite + 1):
        print("".join(str(j) for j in range(1, i + 1)))


n = int(input("Ingrese el número de filas del triángulo: "))
triangulo_numeros(n)