import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def test_setup():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("file:///C:/Users/Master/Desktop/forPythonTests/Test.html")
    yield
    driver.quit()


def test_random(test_setup):
    assert driver.title == "Strona testowa"

