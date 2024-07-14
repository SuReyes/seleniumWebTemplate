from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

text_entered = "Sneakers"


class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.result_text = "//span[@class = 'a-color-state a-text-bold']"

    def validate_search_results(self):
        element = self.driver.find_element(By.XPATH, self.result_text)
        content = element.get_attribute("innerHTML")
        return content

