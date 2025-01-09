from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    SEARCH_RESULTS = (By.XPATH,"//span[@class='h-text-bs h-display-flex h-flex-align-center h-text-grayDark h-margin-l-x2']")

    def verify_search_results(self,product):
        actual_result = self.find_element(*self.SEARCH_RESULTS).text
        assert product in actual_result, f'expected {product} did not match actually actual{actual_result}'
