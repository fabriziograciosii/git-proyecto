def numero_mayor(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

numeros = [4, 12, 7, 45, 2]
print("El número mayor es:", numero_mayor(numeros))