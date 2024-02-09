from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("file:///C:/Users/Master/Desktop/forPythonTests/Test.html")
# driver.maximize_windows()

driver.find_element(By.ID, "clickOnMe").click()

# click_one_me = driver.find_element(By.ID, "clickOnMe")
# click_one_me.click()

driver.find_element(By.TAG_NAME, "p").click()

