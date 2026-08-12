def contar_palabras(frase):
    palabras = frase.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

texto = "hola mundo hola python"
print(contar_palabras(texto))