from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index")
# driver.maximize_window()

driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

draggable = driver.find_element(By.ID, "draggable")
drop_target = driver.find_element(By.ID, "droptarget")

webdriver.ActionChains(driver).drag_and_drop(draggable, drop_target).perform()
