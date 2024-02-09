import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("file:///C:/Users/Master/Desktop/forPythonTests/FileUpload.html")

upload_input = driver.find_element(By.ID, "myFile")
path = os.path.abspath("upload.txt")

upload_input.send_keys(path)

driver.save_screenshot("screenshots/screenshot.png")
