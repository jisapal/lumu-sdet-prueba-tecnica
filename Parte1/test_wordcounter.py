from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def leer_top(driver):
    filas = driver.find_elements(By.CSS_SELECTOR, 'a.list-group-item')
    top = []
    for fila in filas:
        palabra = fila.find_element(By.CSS_SELECTOR, 'span.word').text
        cantidad = int(fila.find_element(By.CSS_SELECTOR, 'span.badge').text.split()[0])
        top.append((palabra, cantidad))
    return top

def correr_escenario(driver, texto, esperado_palabras, esperado_caracteres, esperado_top):
    # 1. cargar la página
    driver.get("https://wordcounter.net/")
    # 2. escribir el texto en la caja
    driver.find_element(By.ID, "box").send_keys(texto)   
    time.sleep(1)
    # 3. leer contador y top  
    contador = driver.find_element(By.CSS_SELECTOR, 'span[data-tr-detail="words_characters"]')
    trozos = contador.text.split()
    palabras = int(trozos[0])
    caracteres = int(trozos[2])
    top = leer_top(driver)
    for intento in range(10):
        if top[:3] == esperado_top:
            break
        time.sleep(0.5)
        top = leer_top(driver)
    # 4. las tres comparaciones

    fallos = []

    if palabras == esperado_palabras:
            print("PASS palabras")
    else:
            print(f"FAIL palabras: esperaba {esperado_palabras} pero salió {palabras}")
            fallos.append(f"palabras: esperaba {esperado_palabras} pero salió {palabras}")
    if caracteres == esperado_caracteres:
            print("PASS caracteres")
    else:
            print(f"FAIL caracteres: esperaba {esperado_caracteres} pero salió {caracteres}")
            fallos.append(f"caracteres: esperaba {esperado_caracteres} pero salió {caracteres}")
    top3 = top[:3]  
    
    if top3 == esperado_top:
            print("PASS top3")
    else:
            print(f"FAIL top3: esperaba {esperado_top} pero salió {top3}")
            fallos.append(f"top3: esperaba {esperado_top} pero salió {top3}")
    return fallos

escenarios = [
    {"id": "S01", "texto": "lumu lumu lumu illuminates illuminates attacks", "palabras": 6, "caracteres": 46, "top": [('lumu', 3), ('illuminates', 2), ('attacks', 1)]},
    {"id": "S02", "texto": "lumu lumu lumu lumu lumu illuminates illuminates attacks and adversaries\nlumu illuminates all attacks and adversaries", "palabras": 16, "caracteres": 116, "top": [('lumu', 6), ('illuminates', 3), ('attacks', 2)]},
    {"id": "S03", "texto": "Lumu lumu lumu lumu lumu Illuminates illuminates attacks AND adversaries\nlumu illuminates all attacks and adversaries", "palabras": 16, "caracteres": 116, "top": [('lumu', 6), ('illuminates', 3), ('attacks', 2)]},
    {"id": "S04", "texto": "Lumu, lumu lumu lumu lumu. Illuminates illuminates attacks AND adversaries!\nlumu illuminates all attacks and adversaries.", "palabras": 16, "caracteres": 120, "top": [('lumu', 6), ('illuminates', 3), ('attacks', 2)]},
    {"id": "S05", "texto": "Lumu lumu lumu lumu lumu\nIlluminates illuminates\nattacks AND adversaries\nlumu illuminates\nall attacks and adversaries", "palabras": 16, "caracteres": 114, "top": [('lumu', 6), ('illuminates', 3), ('attacks', 2)]},
    {"id": "S06", "texto": "...", "palabras": 0, "caracteres": 3, "top": []},
    {"id": "S07", "texto": ".... and all", "palabras": 2, "caracteres": 12, "top": [('all', 1)]},
    {"id": "S08", "texto": "😀😃😄", "palabras": 1, "caracteres": 6, "top": [('😀😃😄', 1)]},
    {"id": "S09", "texto": "      ", "palabras": 0, "caracteres": 6, "top": []},
]

pasaron = 0
fallaron = 0
errores = []

for e in escenarios:
    driver = webdriver.Chrome()
    print(e["id"])
    resultado = correr_escenario(driver, e["texto"], e["palabras"], e["caracteres"], e["top"])
    if resultado == []:
        pasaron = pasaron + 1
    else:
        fallaron = fallaron + 1
        errores.append(f"{e['id']}: {resultado}")
    driver.quit()
print()
print("Ejecutados:", len(escenarios))
print("Pasaron:", pasaron)
print("Fallaron:", fallaron)
for error in errores:
    print(error)