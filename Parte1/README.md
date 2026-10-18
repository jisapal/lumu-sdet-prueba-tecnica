# Parte 1 – Pruebas automatizadas de wordcounter.net

Suite en Python + Selenium que valida, en https://wordcounter.net/:

- el conteo de **palabras**,
- el conteo de **caracteres** (los saltos de línea no cuentan, ni como carácter ni como palabra),
- el **top 3 de Keyword Density** (la página excluye por defecto las palabras comunes, como `and`; solo se prueba lo que muestra).

Al final imprime un resumen: escenarios ejecutados, pasados, fallados y la descripción de cada error.

## Requisitos

- Python 3.9 o superior
- Google Chrome instalado
- Conexión a internet (Selenium descarga el driver de Chrome automáticamente)

## Instalación

```bash
git clone <URL-DEL-REPOSITORIO>
cd <carpeta-del-repositorio>/Parte1
```

## Cómo ejecutar

```bash
python3 test_wordcounter.py
```

Se abre un navegador por escenario, ejecuta la prueba y el script lo cierra solo.

> En macOS puede aparecer un aviso `NotOpenSSLWarning`. Es inofensivo y no afecta las pruebas.

## Ejemplo de salida

```
S01
PASS palabras
PASS caracteres
PASS top3
...
Ejecutados: 9
Pasaron: 9
Fallaron: 0
```

Si un escenario falla, se ve el motivo, por ejemplo:

```
Ejecutados: 9
Pasaron: 8
Fallaron: 1
S05: ['caracteres: esperaba 114 pero salió 113']
```

## Escenarios
Texto base:
lumu lumu lumu lumu lumu illuminates illuminates attacks and adversaries
lumu illuminates all attacks and adversaries

Partiendo de este texto, se han creado los siguientes escenarios

| Id  |            Texto de entrada                      | Palabras | Caracteres |           Top 3 esperado         |   Tipo   |
|-----|--------------------------------------------------|----------|------------|----------------------------------|----------|
| S01 | `lumu lumu lumu illuminates illuminates attacks` |     6    |      46    | lumu 3, illuminates 2, attacks 1 | Estricto |
| S02 | Texto del enunciado (Texto Original)             |    16    |     116    | lumu 6, illuminates 3, attacks 2 | Estricto |
| S03 | Texto con mayúsculas mezcladas (`Lumu`, `Illuminates`, `AND`) |    16    |     116    | lumu 6, illuminates 3, attacks 2 | Suposición: no distingue mayúsculas |
| S04 | Texto con comas, puntos y signos                 |    16    |     120    | lumu 6, illuminates 3, attacks 2 | Suposición: la puntuación no separa palabras |
| S05 | Igual a S02 con varios saltos de línea           |    16    |     113    | lumu 6, illuminates 3, attacks 2 | Estricto: los saltos no cuentan |
| S06 | `...`                                            |     0    |       3    | (vacío)                          | Observado |
| S07 | `.... and all`                                   |     2    |      12    | all 1                            | Observado |
| S08 | `😀😃😄`                                         |     1    |       6    | `😀😃😄` 1                       | Observado |
| S09 | Seis espacios en blanco                          |     0    |       6    | (vacío)                          | Observado |

- **Estricto:** sale del enunciado o de lo que confirmó Lumu.
- **Suposición:** criterio mío, documentado.
- **Observado:** valor que la página muestra hoy; no necesariamente es el comportamiento correcto.

Orden del top 3 en caso de empate: por orden de aparición en el texto (comprobado en la página).

## Cómo funciona

1. `leer_top(driver)` lee las filas de Keyword Density y devuelve una lista de pares (palabra, cantidad).
2. `correr_escenario(...)` abre la página, escribe el texto, lee el contador y el top, compara con lo esperado y devuelve una lista si falla si la lista está vacía, el escenario pasó.
3. El bucle principal recorre la lista de escenarios, abre un navegador nuevo por cada uno y acumula los resultados.
4. Al final imprime el resumen.

Decisiones:

- **Un navegador nuevo por escenario.** La página recuerda el texto de la visita anterior y lo concatena con el nuevo, por lo que un escenario contaminaba al siguiente.
- **Reintento al leer el top.** Keyword Density tarda un instante en actualizarse. Se vuelve a leer hasta 10 veces, cada 0,5 s, antes de dar el resultado.
- **Locators:** caja de texto `#box`, contador `span[data-tr-detail="words_characters"]`, filas de Keyword Density `a.list-group-item` con `span.word` y `span.badge`.

## Limitaciones

- Depende de la estructura actual de la página: si cambian los selectores, hay que actualizarlos.
- Los escenarios "Observado" documentan el comportamiento de hoy.
- Se probó en Chrome, macOS, Python 3.9.6, Selenium 4.36.0.