# 4 - WORD FREQUENCY COUNTER

Programa en Python que lee un archivo de texto e imprime la cantidad de
palabras, la cantidad de caracteres, la frecuencia de cada palabra de mayor
a menor y un histograma.

## Cómo ejecutar

Requiere Python 3 (probado con 3.9.6). No usa librerías externas.

    cd Parte4
    python3 word_frequency.py

El programa lee el archivo `sample.txt` de la misma carpeta.

## Ejemplo de salida (con sample.txt)

    16 words
    116 characters
    lumu: 6
    illuminates: 3
    attacks: 2
    and: 2
    adversaries: 2
    all: 1

    frecuencia
    lumu ###### 6
    illuminates ### 3
    attacks ## 2
    and ## 2
    adversaries ## 2
    all # 1

## Cómo funciona

1. Lee el archivo y separa el texto en palabras con `split()`.
2. Cuenta cada palabra con un diccionario (si existe suma 1, si no la crea en 1).
3. Convierte el diccionario en una lista de pares (palabra, veces).
4. Ordena la lista de mayor a menor con un ordenamiento por selección escrito
   a mano, sin usar `sorted()` ni `.sort()`.
5. Imprime la lista y el histograma (un `#` por cada vez que aparece la palabra).

## Supuestos

- Los saltos de línea no cuentan como caracteres ni como palabras (116
  caracteres en el ejemplo). Lumu lo confirmó por correo.
- El ejemplo del enunciado muestra `and: 1`, pero en el texto aparece dos
  veces. Lumu confirmó que el valor correcto es `and: 2`.
- Palabras con distinta capitalización (se realiza prueba para confirmar el resultado) se cuentan por separado (`Lumu` y `lumu` son dos palabras)
- La puntuación pegada a la palabra no se elimina (`lumu,` y `lumu.` son
  palabras distintas). Se realiza prueba para confirmar el resultado
- Se realiza la prueba para garantizar que un archivo vacío no rompe el programa: imprime `0 words` y `0 characters`.
- Si dos palabras tienen la misma frecuencia, el orden entre ellas no está
  garantizado.

## Complejidad

Sea `n` el total de palabras y `k` las palabras distintas.
“La notación O() indica cómo crece el trabajo del programa cuando crecen los datos.”

| Paso | Tiempo | Con sample.txt |
|------|--------|----------------|
| Leer y separar con `split()` | O(n) | 16 palabras |
| Contar con diccionario | O(n) | 16 vueltas del `for` |
| Ordenamiento por selección | O(k²) | 15 comparaciones |
| Imprimir | O(k) | 6 líneas |
| **Total** | **O(n + k²)** | |

### Ejemplo con sample.txt (n = 16, k = 6)

El ordenamiento tiene dos `for` anidados. El de afuera da `k - 1 = 5` vueltas
y el de adentro recorre cada vez menos posiciones:

| Vuelta (`inicio`) | Comparaciones |
|-------------------|---------------|
| 0 | 5 |
| 1 | 4 |
| 2 | 3 |
| 3 | 2 |
| 4 | 1 |
| **Total** | **15** |

En general son `k × (k - 1) / 2` comparaciones, que es del orden de k², por
eso es O(k²). Con k = 6 son 15 comparaciones. Si k fuera 10 serían 45, y con
k = 100 serían 4950: si las palabras distintas se multiplican por 10, el
trabajo se multiplica por unas 100.

### Qué domina

- Si casi todas las palabras se repiten, `k` es pequeño y domina el conteo
  (O(n)). Ejemplo: 1.000.000 de palabras y solo 50 distintas → 1.000.000 de
  vueltas de conteo contra 1225 comparaciones al ordenar.
- Si casi todas son distintas, `k` se acerca a `n` y domina el ordenamiento;
  el peor caso es O(n²). Con k = 1.000.000, serían unas 500.000.000.000
  comparaciones.

### Posible mejora

Un ordenamiento como merge sort bajaría la parte de ordenar de O(k²) a O(k log k).
Se usó selección porque es el más sencillo de explicar y el enunciado pedía un ordenamiento propio.