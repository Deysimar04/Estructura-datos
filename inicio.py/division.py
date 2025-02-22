def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")

    resultado = 0
    es_negativo = (a < 0) != (b < 0) 

    a, b = abs(a), abs(b)  

    while a >= b:  
        a -= b
        resultado += 1

    return -resultado if es_negativo else resultado  
# Ejemplo de uso
num1 = int(input("Ingrese el dividendo: "))
num2 = int(input("Ingrese el divisor: "))
print(f"Resultado: {dividir(num1, num2)}")