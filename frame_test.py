from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("file:///C:/Users/Master/Desktop/forPythonTests/iFrameTest.html")
# driver.maximize_windows()

print(driver.find_element(By.TAG_NAME, "h1").text)

# switching to iframe
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
print(driver.find_element(By.TAG_NAME, "h1").text)

# return to default page
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h1").text)
