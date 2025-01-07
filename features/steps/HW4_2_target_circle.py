from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@given('open the target circle page')
def open_main(context):
 context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')

 @then('I should see at least 10 benefit cells')
 def step_then_i_should_see_at_least_10_benefit_cells(context):
  context.driver.find_elements(By.CSS_SELECTOR, '.benefit-cell-class')
expected_result='benefit cells'
assert len(expected_result) >= 10, f"Expected at least 10 benefit cells, but found {len(expected_result)}"
print('passed')
sleep(3)


