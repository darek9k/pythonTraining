from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("file:///C:/Users/Master/Desktop/forPythonTests/Test.html")
# driver.maximize_windows()

print(driver.find_element(By.TAG_NAME, "h1").text)

print(driver.find_element(By.ID, "clickOnMe").text)

# retrieving text form input
driver.find_element(By.ID, "fname").send_keys("Joe")
print(driver.find_element(By.ID, "fname").get_attribute("value"))

# retrieving texts from a hidden element
print(driver.find_element(By.TAG_NAME, "p").get_attribute("textContent"))
