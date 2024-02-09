from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


class WaitForListSize:
    def __init__(self, locator, expected_size):
        self.locator = locator
        self.expected_size = expected_size

    def __call__(self, driver):
        return len(driver.find_elements(By.XPATH, self.locator)) == self.expected_size


# driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10, 0.5)

driver.get("file:///C:/Users/Master/Desktop/forPythonTests/Waits.html")
driver.find_element(By.ID, "clickOnMe").click()
# wait.until(EC.visibility_of_element_located((By.TAG_NAME, "p")))

# Custom condition using lambda expression
# wait.until(lambda wd: len(wd.find_elements(By.TAG_NAME, "p")) == 1)

wait.until(WaitForListSize("//p", 1))
print(driver.find_element(By.TAG_NAME, "p").text)
