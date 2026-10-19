# Parte 3: Reporte de UX

- **URL probada:** https://www.colsubsidio.com/

- **Fecha:** 18 de octubre de 2026

- **Entorno:** Google Chrome, macOS

## Problema 1: Las etiquetas “NUEVA SEDE” y "SEDE ALIADA" tapan la barra de pestañas

**Qué falla:**
Al hacer scroll, las etiquetas de las tarjetas pasan sobre la barra fija. La barra de pestañas debe quedar siempre por encima de las tarjetas, sin que ninguna etiqueta se vea sobre ella.

**Cómo reproducirlo:**
1. Entrar a https://www.colsubsidio.com/
2. Ir a Deportes → Natación.
3. Hacer scroll hasta “Sedes externas” 
4. Hacer clic en “Descúbrelas”.
5. Hacer clic en la pestaña “Sedes de Colsubsidio”.
6. Hacer scroll hacia arriba o hacia abajo por las tarjetas.
7. Mirar la barra de pestañas mientras las tarjetas se deslizan.

**Evidencia:**
![Etiqueta NUEVA SEDE sobre la barra de pestañas](evidencias/problema1-etiquetas.mp4)

**Impacto en el usuario:**
Las etiquetas en las tarjetas se superponen a las opciones que estan en la barra de las sedes. Las pestañas se leen mal y a pantalla se ve rota.


## Problema 2: Pierdes el contexto al abrir una sede

**Qué falla:**
Estoy consultando sedes de natación. Cuando hago clic en “Conoce más” en una sede ejemplo BLOC Fontanar la pagina muestra todos los deportes de la sede, sin filtrar por natación. Esperaba ver primero la natación, o al menos tener el filtro ya aplicado.

**Cómo reproducirlo:**
1. Entrar a https://www.colsubsidio.com/
2. Ir a Deportes → Natación.
3. Hacer scroll hasta “Sedes externas” 
4. Hacer clic en “Descúbrelas”.
5. Hacer clic en la pestaña “Sedes de Colsubsidio”.
6. Hacer clic en Conoce más de BLOC Fontanar
7. Observar la página de la sede: lista todos los deportes y el filtro por ‘Área’ está sin seleccionar.

**Evidencia:**
![Pierdes el contexto al abrir una sede](evidencias/problema2-contexto.mp4)

**Impacto en el usuario:**
Pierdo el contexto: veo todos los deportes que se imparten en esa sede y tengo que volver a filtrar por natación


## Problema 3: Se abre otra pestaña con otra URL sin avisar al entrar a “Sedes externas”
**Qué falla:**
Al hacer clic en ‘Descúbrelas’, se abre una pestaña nueva con una dirección distinta (diversioncolsubsidio.com). El usuario no recibe ningún aviso de que sera redirigido a otra pagina.

**Cómo reproducirlo:**
1. Entrar a https://www.colsubsidio.com/
2. Ir a Deportes → Natación.
3. Hacer scroll hasta “Sedes externas” 
4. Hacer clic en “Descúbrelas”.

**Evidencia:** 
![otra pestaña con otra URL](evidencias/problema3-otraURL.mp4)

**Impacto en el usuario:**
El botón Atrás esta desactivado, y tengo que cerrar la pestaña o cambiar a la pestaña anterior si quiero ver la pagina principal de Colsubsidio.