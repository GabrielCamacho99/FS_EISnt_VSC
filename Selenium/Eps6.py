from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.implicitly_wait(5)

driver.get("https://www.letskodeit.com/practice")

title = driver.find_element(By.TAG_NAME, "h1").text
print(title)

el1 = driver.find_element(By.XPATH, "//legend[contains(text(), 'Checkbox Example')]").text
el2 = driver.find_element(By.XPATH, "//*[@id='checkbox-example-div']/fieldset/label[3]").text

print(f"The elements extracted from the page are: a div title [{el1}] and a checkbox title [{el2}]")

driver.find_element(By.TAG_NAME, "a").click()

driver.save_screenshot("Selenium\\resultado.png")

elements = title, el1, el2

with open("Selenium\\elements.txt", "w") as f:
    for element in elements:
        f.write(f"{element}\n")

print("Screenshot saved as 'resultado.png' and extracted elements saved as 'elements.txt' in the Selenium directory.")
print("Chrome is still open!")

