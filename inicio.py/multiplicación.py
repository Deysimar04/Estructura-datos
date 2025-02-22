def multiplicar(a, b):
    resultado = 0
    es_negativo = (a < 0) != (b < 0) 

    a, b = abs(a), abs(b)  
    for _ in range(b): 
        resultado += a

    return -resultado if es_negativo else resultado  
# Ejemplo de uso
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print(f"Resultado: {multiplicar(num1, num2)}")