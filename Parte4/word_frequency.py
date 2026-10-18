archivo = open("sample.txt")
texto = archivo.read()
archivo.close()

sin_salto = texto.replace("\n", "")#Guardo el texto sin salto de línea en una variable aparte, para conservar el original, que necesito para contar las palabras

parte = texto.split()
print(f"{len(parte)} words")
print(f"{len(sin_salto)} characters")
conteo = {}
for palabra in parte:
   if palabra in conteo:
        conteo[palabra] = conteo[palabra] + 1
   else:
        conteo[palabra] = 1

pares = list(conteo.items()) 
for inicio in range (len(pares)-1):
    posicion_mayor = inicio
    for i in range(inicio+1, len(pares)):
        if pares[i][1] > pares[posicion_mayor][1]:
            posicion_mayor = i
    pares[inicio], pares[posicion_mayor] = pares[posicion_mayor], pares[inicio]

for palabra, veces in pares:
        print(f"{palabra}: {veces}")

print()
print("frecuencia")
for palabra, veces in pares:
        print(f"{palabra} {'#' * veces} {veces}")
