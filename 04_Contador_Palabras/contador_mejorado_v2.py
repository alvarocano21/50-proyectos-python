textoUsuario = input("Introduce un texto: ").strip()

# Normalizamos a minúsculas
texto_normalizado = textoUsuario.lower()

# Palabras
palabras = texto_normalizado.split()
num_palabras = len(palabras)

# Caracteres
num_caracteres = len(textoUsuario)
num_caracteres_sin_espacios = len(textoUsuario.replace(" ", ""))

# Frases (contando puntos)
num_frases = textoUsuario.count(".")

# Frecuencia de palabras
frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print("\n Resultados:")
print("Palabras:", num_palabras)
print("Caracteres (con espacios):", num_caracteres)
print("Caracteres (sin espacios):", num_caracteres_sin_espacios)
print("Frases:", num_frases)

print("\nFrecuencia de palabras:")
for palabra, cantidad in frecuencia.items():
    print(palabra, ":", cantidad)