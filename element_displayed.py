from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("file:///C:/Users/Master/Desktop/forPythonTests/Test.html")

paragraph = driver.find_element(By.TAG_NAME, "p")

if paragraph.is_displayed():
    print(paragraph.text)
else:
    print("Element is not displayed")
    print(paragraph.get_attribute("textContent"))
