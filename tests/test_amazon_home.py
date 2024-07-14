import time

import pytest

from pages.amazon_home_page import HomePage
from pages.amazon_result_page import SearchResultPage
from util.file_reader import read_file_lines


search_terms = read_file_lines("searchterms.csv")


@pytest.mark.usefixtures("driver_setup")
class TestTwitch:

    @pytest.fixture(autouse=True)
    def class_setup(self, driver_setup):
        self.home = HomePage(self.driver)
        self.results = SearchResultPage(self.driver)

    @pytest.mark.parametrize("search_term", search_terms)
    def test_amazon_search(self, search_term):
        # Step 1 go to Amazon
        self.home.open()
        self.home.enter_search_input(search_term)
        text_found = self.results.validate_search_results()
        assert search_term in text_found, f"Search did not find {search_term} results in {text_found}"
