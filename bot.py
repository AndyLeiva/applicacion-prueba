from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='webdrivers\chromedriver.exe')
driver.get('https://andyleiva.github.io/applicacion-prueba/')


driver.find_element_by_xpath('//*[@id="botonclick"]')
driver.click()
