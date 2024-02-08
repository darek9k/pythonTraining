from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("file:///C:/Users/Master/Desktop/forPythonTests/Test.html")
# driver.maximize_windows()

# send_keys method
driver.find_element(By.ID, "fname").send_keys("Joe")

driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
