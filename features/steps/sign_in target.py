from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@given("Open Target Page")
def open_main(context):
    context.driver.get('https://www.target.com/')

@when("click on sign in")
def click_sign_in(context):
    context.driver.find_element(By.ID,"account-sign-in").click()
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

@then("verify sign in page")
def verify_search_results(context):
 expected = 'Sign into your Target account'
 actual = context.driver.find_element(By.XPATH, "//h1/span").text
 assert expected == actual, f'expected{expected} did not match actually actual{actual}'
