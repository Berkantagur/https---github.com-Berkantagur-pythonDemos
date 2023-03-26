from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com/")
input = driver.find_element(By.NAME, "q")
print(f"Input: {input}")

# sleep(10)
while True:
    continue

# HTML LOCATORS
