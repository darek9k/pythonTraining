import allure
import pytest

from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_results import SearchResultPage
from page_object_pattern.utils.read_excel import ExcelReader


@pytest.mark.usefixtures("setup")
class TestHotelSearch:

    @allure.title("Test Hotel Search")
    @allure.description("Test description")
    @pytest.mark.parametrize("data", ExcelReader.get_data())
    def test_hotel_search(self, data):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city('Dubai')
        search_hotel_page.set_date_range(data.check_in, data.check_out)
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
