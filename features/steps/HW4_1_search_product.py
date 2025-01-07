from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("open the target page")
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('search for {Search_Product}')
def search_product(context,Search_Product):
    context.driver.find_element(By.ID,'search').send_keys(Search_Product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

@then('i should see the results')
def i_should_see(context):
    expected_result = 'table'
    actual_result = context.driver.find_element(By.XPATH,"//span[@class='h-text-bs h-display-flex h-flex-align-center h-text-grayDark h-margin-l-x2']").text
    assert expected_result in actual_result, f'expected{expected_result} did not match actually actual{actual_result}'
    print('passed')

sleep(5)


