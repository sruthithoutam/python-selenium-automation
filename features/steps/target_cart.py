from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("open the target main page")
def open_main(context):
 context.driver.get('https://www.target.com/')
 
@when("click on cart")
def click_cart(context):
 context.driver.find_element(By.CSS_SELECTOR, "[href='/cart?prehydrateClick=true']").click()
 sleep(2)

 @then("Verify that cart is empty")
 def verify_that_cart_is_empty(context):
  expected_result ='Your cart is empty'
  actual_result=context.driver.find_element(By.CSS_SELECTOR, "h1[class='sc-fe064f5c-0 fJliSz']").text
  assert expected_result==actual_result,f'expected{expected_result} did not match actually actual{actual_result}'
print('passed')
