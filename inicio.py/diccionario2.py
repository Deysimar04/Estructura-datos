def triangulo_numeros(n):
    for i in range(1, n + 1):
        print("".join(str(j) for j in range(1, i + 1)))

# Ejemplo de uso
triangulo_numeros(5)
