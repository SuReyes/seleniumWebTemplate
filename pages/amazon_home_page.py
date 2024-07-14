from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


text_to_search = "Sneakers"


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.page_url = 'https://www.amazon.com/'
        self.input = "twotabsearchtextbox"

    def open(self):
        self.driver.get(self.page_url)

    def enter_search_input(self, search_term=text_to_search):
        element = self.driver.find_element(By.ID, self.input)
        element.click()
        element.send_keys(search_term)
        element.send_keys(Keys.ENTER)
