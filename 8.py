def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in frase:
        if letra in vocales:
            contador += 1
    return contador

print("Vocales en 'Murcielago':", contar_vocales("Murcielago"))
print("Vocales en 'Python es genial':", contar_vocales("Python es genial"))