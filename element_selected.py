from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("file:///C:/Users/Master/Desktop/forPythonTests/Test.html")

checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")

# checkbox.click()

if checkbox.is_selected():
    print("Element is selected")
else:
    print("Element is not selected. Im clicking on it")
    checkbox.click()
