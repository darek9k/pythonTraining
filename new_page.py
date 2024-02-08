from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("file:///C:/Users/Master/Desktop/forPythonTests/Test.html")
# driver.maximize_windows()

driver.find_element(By.ID, "newPage").click()
print(driver.title)

current_windows_name = driver.current_window_handle
window_names = driver.window_handles

for window in window_names:
    if window != current_windows_name:
        driver.switch_to.window(window)

print(driver.title)
