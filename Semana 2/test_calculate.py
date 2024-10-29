from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def probar_calculo(num1, num2, operador, resultado_esperado):
    driver.get("http://127.0.0.1:5000")  # URL de la aplicación Flask

    # Esperar hasta que el campo num1 esté disponible
    input_num1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "num1"))
    )
    input_num1.clear()
    input_num1.send_keys(num1)

    # Esperar hasta que el campo num2 esté disponible
    input_num2 = driver.find_element(By.NAME, "num2")
    input_num2.clear()
    input_num2.send_keys(num2)

    # Seleccionar el operador
    select_operator = driver.find_element(By.NAME, "operator")
    select_operator.send_keys(operador)  # O puedes usar select_operator.select_by_visible_text(operador)

    # Hacer clic en el botón "Calcular"
    btn_calcular = driver.find_element(By.XPATH, "//input[@type='submit']")
    btn_calcular.click()

    # Obtener el resultado de la página
    resultado_pagina = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p"))
    ).text

    # Comparar el resultado obtenido con el esperado
    if resultado_pagina == resultado_esperado:
        print(f"Prueba exitosa para {num1} {operador} {num2}")
    else:
        print(f"La prueba falló para {num1} {operador} {num2}")

# Ejecutar las pruebas
probar_calculo(5, 3, "sumar", "8")  # Cambia el resultado esperado según tu lógica
probar_calculo(5, 3, "restar", "2")  # Cambia el resultado esperado según tu lógica
probar_calculo(5, 3, "multiplicar", "15")  # Cambia el resultado esperado según tu lógica
probar_calculo(5, 3, "dividir", "1.67")  # Cambia el resultado esperado según tu lógica

# Cerrar el navegador
driver.quit()
