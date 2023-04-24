from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open search results page')
def open_search_results_page(context):
    context.driver.get('https://shop.cureskin.com/search?q=cure')

@then('Verify first results have name, image, and price')
def verify_first_results(context):
    context.app.cureskin_search.verify_first_results()