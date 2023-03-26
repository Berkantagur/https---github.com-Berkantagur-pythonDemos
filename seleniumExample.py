# Selenium is an open source automation testing tool that supports a number of scripting languages
# like Python, C#, Java, Perl, Ruby, JavaScript, etc. depending on the application to be tested. 

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
