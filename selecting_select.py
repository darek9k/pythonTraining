from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("file:///C:/Users/Master/Desktop/forPythonTests/Test.html")
# driver.maximize_windows()
auto_select = Select(driver.find_element(By.TAG_NAME, "select"))
auto_select.select_by_visible_text("Volvo")
auto_select.select_by_value("saab")
auto_select.select_by_index(2)
