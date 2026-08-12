def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

print("¿El 11 es primo?", es_primo(11))
print("¿El 12 es primo?", es_primo(12))