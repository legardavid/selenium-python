from selenium import webdriver
import time
browser2 = webdriver.Edge()

#Precio del Bitcoin con Web Scraping (Python y Selenium)

PATH = 'C:\path\to\msedgedriver.exe'

#driver = webdriver.Edge(executable_path=r'C:\path\to\msedgedriver.exe')
driver = webdriver.Edge(PATH)

driver.get("https://es.investing.com/crypto/bitcoin")

time.sleep(5)

precioBTC = driver.find_element_by_xpath('//*[@id="last_last"]')

print('Precio del Bitcoin: '+ precioBTC.text)

driver.quit()