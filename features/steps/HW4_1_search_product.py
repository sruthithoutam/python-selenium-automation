from behave import given, when, then
from time import sleep

@given("open the target page")
def open_main(context):
    context.app.main_page.open_main()

@when('search for {Search_Product}')
def search_product(context,Search_Product):
    context.app.header.search_product(Search_Product)

@then('i should see the results for {Search_Product}')
def i_should_see(context,Search_Product):
    context.app.search_results_page.verify_search_results(Search_Product)
    print('passed')

sleep(5)


