from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://w3schools.com")

driver.find_element(By.ID, "accept-choices").click()

tutorials_element = driver.find_element(By.XPATH, "//*[@id='subtopnav']/a[1]")
webdriver.ActionChains(driver).move_to_element(tutorials_element).click(tutorials_element).perform()
