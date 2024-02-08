from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("file:///C:/Users/Master/Desktop/forPythonTests/Test.html")
# driver.maximize_windows()

driver.find_element(By.ID, "clickOnMe")
driver.find_element(By.NAME, "fname")
driver.find_element(By.LINK_TEXT, "Visit W3Schools.com!")
driver.find_element(By.PARTIAL_LINK_TEXT, "Visit W3Schools.com")
driver.find_element(By.CLASS_NAME, "topSecret")
driver.find_element(By.TAG_NAME, "a")
driver.find_element(By.TAG_NAME, "p")

# css selectors
driver.find_element(By.CSS_SELECTOR, "a")
driver.find_element(By.CSS_SELECTOR, "img#smileImage")
driver.find_element(By.CSS_SELECTOR, "p.topSecret")
print(driver.find_element(By.CSS_SELECTOR, "th:first-child").text)


# xpath
driver.find_element(By.XPATH, "/html/body/table/tbody/tr/th")
driver.find_element(By.XPATH, "//tbody//th")
driver.find_element(By.XPATH, "//th")
driver.find_element(By.XPATH, "//th[text()='Month']")
driver.find_element(By.XPATH, "//button[@id='clickOnMe']")
driver.find_element(By.XPATH, "//input[@id='fname']/following-sibling::table")

# find_elements
print(len(driver.find_elements(By.XPATH, "//th")))


driver.quit()
