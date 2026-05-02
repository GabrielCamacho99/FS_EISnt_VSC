from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://google.com")

search = driver.find_element(By.NAME, "q")
search.send_keys("Python automação")

search.submit()