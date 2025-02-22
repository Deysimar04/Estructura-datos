def arreglo(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + arreglo(arr, n - 1)

numeros = [7, 9, 3, 3, 10, 12]  
resultado = arreglo(numeros, len(numeros))
print(f"Suma de la lista: {resultado}")