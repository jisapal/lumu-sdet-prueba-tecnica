# Prueba técnica – Software Developer Engineer in Test (Lumu Technologies)

Autora: Juana Isabel Palmera Ortega

## Contenido

| Parte | Qué contiene | Carpeta |
|-------|--------------|---------|
| 1 | Suite automatizada (Python + Selenium) que valida conteo de palabras, caracteres y top 3 de Keyword Density en wordcounter.net, con resumen de resultados | [Parte1](Parte1/) |
| 2 | Reporte de fallos encontrados en wordcounter.net | [Parte2](Parte2/REPORTE.md) |
| 3 | Reporte de UX: 3 problemas en un sitio público, con pasos para reproducirlos | [Parte3](Parte3/REPORTE.md) |
| 4 | Contador de frecuencia de palabras con ordenamiento escrito a mano, histograma y explicación de complejidad | [Parte4](Parte4/) |

Cada carpeta tiene su propio README (Partes 1 y 4) con instrucciones de ejecución.

## Cómo ejecutar

Requisitos: Python 3.9 o superior; para la Parte 1, además, Google Chrome y `pip3 install selenium==4.36.0`.

```bash
git clone https://github.com/jisapal/lumu-sdet-prueba-tecnica.git
cd lumu-sdet-prueba-tecnica

# Parte 1
cd Parte1
python3 test_wordcounter.py

# Parte 4 (se ejecuta desde dentro de su carpeta)
cd ../Parte4
python3 word_frequency.py
```

## Aclaraciones de Lumu que seguí

- En el ejemplo del enunciado, `and: 1` es un error de redacción; el valor correcto es `and: 2`.
- Los saltos de línea no cuentan ni como caracteres ni como palabras.
- Keyword Density excluye por defecto las palabras comunes; solo se prueba lo que muestra la página.
- En la Parte 2 reporto lo que considero incorrecto, con cómo debería manejarlo la página.

## Decisiones de diseño destacadas

- **Parte 1:** un navegador nuevo por escenario (la página conserva el texto de la visita anterior), reintento al leer Keyword Density y escenarios separados en "Estricto", "Suposición" y "Observado".
- **Parte 4:** selection sort escrito a mano; la complejidad y los supuestos están explicados en su README.