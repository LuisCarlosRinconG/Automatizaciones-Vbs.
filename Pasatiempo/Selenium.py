from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#función para ingresar a github luego de inspeccionar la pagina y extraer ic,nombre y clase
def ingresar():
    # abrir pagina
    driver = webdriver.Chrome()
    driver.get("https://github.com/")
    time.sleep(10)
    # ingresar al boton "Ingresar"
    ingresar = driver.find_element(By.LINK_TEXT, "Sign in")
    ingresar.click()

    #esperar 5 segundos que cargue la pagina
    time.sleep(5)
    
    #buscar el campo de correo por el id
    ingresar = driver.find_element(By.ID, "login_field")
    ingresar.send_keys('correo')

    #buscar el campo de contraseña por el nombre
    ingresar = driver.find_element(By.NAME, "password")
    ingresar.send_keys('contraseña')

    # buscar el boton para ingresar con la clase
    ingresar = driver.find_element(By.CLASS_NAME, "btn-primary")
    ingresar.click()

    #esperar 5 segundos a que cargue la pagina
    time.sleep(5)

    #salir
    driver.quit()
#-----------------------------------------------------------------------------------------------------------------------------
# Automatizar el proceso de recuperación de cuenta por medio de Partial Link.
def olvido_contraseña():
    # abrir pagina
    driver = webdriver.Chrome()
    driver.get("https://prezi.com/login/?click_source=logged_element&page_location=header&element_text=log_in")
    time.sleep(10)

    # buscar por medio de PARTIAL_LINK_TEXT la opción de ¿olvidaste tu contraseña?
    # busca similitudes
    click_olvidar = driver.find_element(By.PARTIAL_LINK_TEXT, "¿Olvidaste")
    click_olvidar.click()

    time.sleep(5)
    
    restablecer = driver.find_element(By.CLASS_NAME,"bIhtjF")
    restablecer.send_keys("correo")

    clickRestablecer = driver.find_element(By.CLASS_NAME,"ejWXEB")
    clickRestablecer.click()
    time.sleep(5)
    driver.quit()

#-----------------------------------------------------------------------------------------------------------------------------
# Extensión Chropath.

def Chropath():
    # primero se instala la esxtensión Chropath en el navegador firefox
# se inspecciona la pagina a buscar y gracias a Chropath se obtienen -Ruta abosluta- Ruta relativa -Atributos CSS.
    
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/?locale=es_LA")
    time.sleep(10)

    # 1. Ruta relativa
    usuario_ruta_relativa = driver.find_element(By.XPATH, ".//input[@id='email']")
    usuario_ruta_relativa.send_keys("correo")

    # 2. Ruta absoluta
    contrasena_ruta_absoluta = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]")
    contrasena_ruta_absoluta.send_keys("contraseña")

    # 3. Atributos CSS
    boton_ruta_CSS = driver.find_element(By.CSS_SELECTOR, "button[name='login']")
    boton_ruta_CSS.click()
    
    time.sleep(10)
    driver.quit()

# el main desde donde se llaman las funciones creadas
def main():
    while True:
        print('Se hizo uso de varias paginas para validar la funcionalidad de selenium en diferentes entornos')
        print('Escoge una de las opciones:')
        print('1) Ingresar a GitHub')
        print('2) Restablecer contraseña de Prezi')
        print('3) Ingresar a facebook con la información extraida de Chropath')
        print('4) Salir')

        opcion = int(input('Ingresa una opción:\n'))

        if opcion == 1:
            ingresar()
        elif opcion == 2:
            olvido_contraseña()
        elif opcion == 3:
            Chropath()
        elif opcion == 4:
            print('Saliendo...Gracias ;)')
            break
        else:
            print('Escoge una de las opciones mencionadas')
main()
