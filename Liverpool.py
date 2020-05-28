from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\legal\Desktop\Bedu\Phyton\Proyecto\chromedriver.exe")
driver.get("https://proveedores.liverpool.com.mx/irj/portal ")

usuario = driver.find_element_by_id("logonuidfield")
usuario.send_keys("P00112461")

contraseña = driver.find_element_by_id("logonpassfield")
contraseña.send_keys("I1234567")
contraseña.send_keys(Keys.ENTER)

time.sleep(5)
driver.close()
