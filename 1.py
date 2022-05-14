from selenium import webdriver

driver = webdriver.Edge(executable_path=r'C:\path\to\msedgedriver.exe')
driver.get('edge://settings/help')
print("Page title is: %s" %(driver.title))
#driver.quit()