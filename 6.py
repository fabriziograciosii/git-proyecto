def es_palindromo(palabra):
    palabra = palabra.lower() # Convertir a minúsculas
    return palabra == palabra[::-1]

print("¿'Reconocer' es palíndromo?", es_palindromo("Reconocer"))