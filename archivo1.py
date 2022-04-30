from selenium import webdriver
import time

#Precio del Bitcoin con Web Scraping (Python y Selenium)

PATH = 'C:/chrome_webdriver/chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get("https://es.investing.com/crypto/bitcoin")

time.sleep(5)

precioBTC = driver.find_element_by_xpath('//*[@id="last_last"]')

print('Precio del Bitcoin: '+ precioBTC.text)

driver.quit()