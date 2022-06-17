from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

website = "https://www.plazavea.com"
path = "C:\program files (x86)\chromedriver.exe"

class prueba_selenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(path)
    
    def test_buscar_por_nombre(self):
        driver = self.driver
        driver.get(website)
        time.sleep(2)
        login_alerta = driver.find_element_by_css_selector("span.Header__dropdown__iconList__login__notification__close.pvaicon.pvaicon-14-close")
        login_alerta.click()
        time.sleep(2)
        menu_supermercado = driver.find_element_by_css_selector("i.pvaicon.pvaicon-18-menu")
        menu_supermercado.click()
        time.sleep(2)
        selec_preferencias = driver.find_element_by_css_selector("span.textMenu")
        selec_preferencias.click()
        time.sleep(2)
        ver_supermercado = driver.find_element_by_css_selector("li.MainMenu__wrapper__departments__item.link-all")
        ver_supermercado.click()
        time.sleep(2)
        siguiente_banner = driver.find_element_by_css_selector("button.customNav__next")
        siguiente_banner.click()
        time.sleep(2)
        regresar_banner_anterior = driver.find_element_by_css_selector("button.customNav__prev")
        regresar_banner_anterior.click()
        time.sleep(2)
        selec_producto = driver.find_element_by_css_selector("span.CategoryItem__title")
        selec_producto.click()
        time.sleep(2)
        quitar_alerta = driver.find_element_by_css_selector("span.Header__info__preferences__tooltip__close.pvaicon.pvaicon-14-close")
        quitar_alerta.click()
        time.sleep(2)
        ver_promocion = driver.find_element_by_css_selector("img.CustomModal__body__image__dsk")
        ver_promocion.click()
        time.sleep(5)
        
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()