from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("file:///C:/Users/Master/Desktop/forPythonTests/Test.html")

# The find_elements method, if it does not find any elements on the page, creates a list that equals 0
first_name_input = driver.find_elements(By.TAG_NAME, "p")

if len(first_name_input) == 0:
    print("There is no such element on the page")
else:
    print(str(len(first_name_input)) + "5 items found on the page")

try:
    driver.find_element(By.TAG_NAME, "pa")
    print(str(len(first_name_input)) + "5 items found on the page")
except NoSuchElementException:
    print("There is no such element on the page")
