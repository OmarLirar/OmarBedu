from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\legal\Desktop\Bedu\Phyton\Proyecto\chromedriver.exe")
driver.get("http://proveedores.bodegasalianza.com/Secure/Login.aspx?returnurl=%2fhome.aspx")

usuario = driver.find_element_by_id("ctl00_mainContent_login1_LoginCtrl_UserName")
usuario.send_keys("broque")

contraseña = driver.find_element_by_id("ctl00_mainContent_login1_LoginCtrl_Password")
contraseña.send_keys("Jimador20")
contraseña.send_keys(Keys.ENTER)









driver.find_element_by_link_text('Proveedores').click()

time.sleep(5)
driver.find_elements_by_xpath('//*[@id="ctl00_mainContent_ctl00_m_xnvSearchCriterials_GCTC0_m_xbtnExportExcel_I"]')[0].click()

time.sleep(5)
driver.close()
