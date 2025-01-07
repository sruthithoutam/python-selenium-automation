from selenium.webdriver.common.by import By
from behave import then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR,"[data-test='content-wrapper'] [id*='addToCart']")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

@then('Verify search results shown for {product}')
def verify_search_results(context, product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_result, f'Expected text {product} not in actual {actual_result}'

    sleep(2)

@then('click on add to cart button')
def click_add_to_cart(context):
    sleep(5)
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(2)

@then("confirm add to cart button from navigation side")
def confirm_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='content-wrapper'] [id*='addToCartButton']").click()
    sleep(2)

@then('open cart page')
def open_cart_page(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/cart']").click()
    sleep(2)

@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(By.XPATH, "//div[./span[contains(text(), 'subtotal')]]").text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"