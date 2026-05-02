from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://www.ipma.pt/pt/otempo/prev.localidade.hora/")
time.sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.save_screenshot("finalPagina_script.png")

print("Screenshot guardado e Chrome continua aberto!")

