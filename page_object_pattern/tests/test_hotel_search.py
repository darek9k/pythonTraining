import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_results import SearchResultPage


class TestHotelSearch:

    @pytest.fixture()
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    @pytest.mark.test_hotel_search
    def test_hotel_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city('Dubai')
        search_hotel_page.set_date_range("12/02/2024", "15/02/2024")
        search_hotel_page.set_travellers("4", "4")
        search_hotel_page.perform_search()
        results_page = SearchResultPage(self.driver)
        hotel_names = results_page.get_hotel_names()
        price_values = results_page.get_hotel_prices()

        assert hotel_names[0] == 'Jumeirah Beach Hotel'
        assert hotel_names[1] == 'Oasis Beach Tower'
        assert hotel_names[2] == 'Rose Rayhaan Rotana'
        assert hotel_names[3] == 'Hyatt Regency Perth'

        assert price_values[0] == '£14.30'
        assert price_values[1] == '£32.50'
        assert price_values[2] == '£52'
        assert price_values[3] == '£97.50'
