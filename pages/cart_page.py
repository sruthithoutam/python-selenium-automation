from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage

class cart_page(BasePage):
    Cart_BTN = (By.CSS_SELECTOR, "[href='/cart?prehydrateClick=true']")
    SEARCH_RESULT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")

    def click_cart(self):
        self.click(*self.Cart_BTN)
        sleep(10)


    def verify_empty_cart(self):
        expected_result = 'Your cart is empty'
        actual_result = self.find_element(*self.SEARCH_RESULT).text
        assert expected_result == actual_result, f'expected{expected_result} did not match actually actual{actual_result}'

