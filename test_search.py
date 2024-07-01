import pytest
from selenium import webdriver
from pages.search_page import SearchPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_search_name(driver):
    search_page = SearchPage(driver)
    search_page.load()
    search_page.enter_name("Tom Hanks")
    search_page.select_gender("Male")
    search_page.select_born_date("1950-01-01", "1960-01-01")
    search_page.click_search()

    # Add assertions to verify search results
    results = driver.find_elements_by_class_name("lister-item")
    assert len(results) > 0, "No results found"