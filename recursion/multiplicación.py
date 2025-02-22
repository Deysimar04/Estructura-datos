def multiplicacion(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + multiplicacion(a, b - 1)

print(multiplicacion(2, 5))  
print(multiplicacion(7, 4))