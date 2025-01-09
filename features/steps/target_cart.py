from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("open the target main page")
def open_main(context):
 context.app.main_page.open_main()
 
@when("click on cart")
def click_cart(context):
 context.app.cart_page.click_cart()

 @then("Verify that cart is empty")
 def verify_that_cart_is_empty(context):
  context.app.cart_page.verify_empty_cart()
  print('passed')
