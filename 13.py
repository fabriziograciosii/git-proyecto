def fibonacci(n):
    secuencia = [0, 1]
    for i in range(2, n):
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
    return secuencia[:n]

print("Primeros 8 números de Fibonacci:", fibonacci(8))
print("Primeros 12 números de Fibonacci:", fibonacci(12))