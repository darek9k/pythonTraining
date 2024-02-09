from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo/")

driver.find_element(By.XPATH, "//span[text()='Search by Hotel or City Name']").click()
driver.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys('Dubai')
driver.find_element(By.XPATH, "//span[text()='Dubai']").click()
driver.find_element(By.NAME, "checkin").send_keys("09/02/2024")
driver.find_element(By.NAME, "checkout").send_keys("15/02/2024")
# interaction with the calendar / code bellow
driver.find_element(By.ID, "travellersInput").click()
driver.find_element(By.ID, "adultInput").clear()
driver.find_element(By.ID, "adultInput").send_keys("4")
driver.find_element(By.ID, "childInput").clear()
driver.find_element(By.ID, "childInput").send_keys("4")
driver.find_element(By.ID, "travellersInput").click()
driver.find_element(By.XPATH, "//button[text()=' Search']").click()

hotels = driver.find_elements(By.XPATH, "//h4[contains(@class,'list_title')]//b")
hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]
for name in hotel_names:
    print("Hotel name: " + name)

prices = driver.find_elements(By.XPATH, "//div[contains(@class,'price_tab')]//b")
price_values = [price.get_attribute("textContent") for price in prices]
for price in price_values:
    print("Price " + price)

assert hotel_names[0] == 'Jumeirah Beach Hotel'
assert hotel_names[1] == 'Oasis Beach Tower'
assert hotel_names[2] == 'Rose Rayhaan Rotana'
assert hotel_names[3] == 'Hyatt Regency Perth'
assert price_values[0] == '£14.30'
assert price_values[1] == '£32.50'
assert price_values[2] == '£52'
assert price_values[3] == '£97.50'

driver.quit()

# interaction with the calendar / code bellow
# driver.find_element(By.NAME, "checkin").click()
# driver.find_element(By.XPATH, "//td[@class='day  active']").click()
#
# # we use the list and search for the visible one - after this xpath there are as many as 7 elements on the page
# elements = driver.find_elements(By.XPATH, "//td[@class='day ' and text()='15']")
# for element in elements:
#     if element.is_displayed():
#         element.click()
#         break
