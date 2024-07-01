from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    URL = "https://www.imdb.com/search/name/"

    def _init_(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def load(self):
        self.driver.get(self.URL)

    def enter_name(self, name):
        name_input = self.wait.until(EC.presence_of_element_located((By.ID, "name")))
        name_input.send_keys(name)

    def select_gender(self, gender):
        gender_select = self.wait.until(EC.element_to_be_clickable((By.ID, "gender")))
        for option in gender_select.find_elements(By.TAG_NAME, 'option'):
            if option.text == gender:
                option.click()
                break

    def select_born_date(self, from_date, to_date):
        born_date_from = self.wait.until(EC.presence_of_element_located((By.ID, "birth_date_min")))
        born_date_to = self.wait.until(EC.presence_of_element_located((By.ID, "birth_date_max")))
        born_date_from.send_keys(from_date)
        born_date_to.send_keys(to_date)

    def click_search(self):
        search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Search')]")))
        search_button.click()