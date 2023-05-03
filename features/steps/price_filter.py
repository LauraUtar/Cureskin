from selenium.webdriver.common.by import By
from behave import given, when, then



@given('Open cureskin homepage')
def open_cireskin_homepe(context):
    context.driver.get('https://shop.cureskin.com/')


@when('Close popup window')
def close_window(context):
    context.app.main_page.close_popup_window()
    from time import sleep
    #sleep(5)



@then("Click on Shop All section")
def click_shop_all(context):
    context.app.main_page.click_shop_all()


@then('Adjust the Price Filter such that there is a change in number of products')
def adjust_price_filter(context):
    context.app.main_page.adjust_price_filter()


@then("Verify that number of products changes")
def verify_product_number_change(context):
    context.app.main_page.verify_number_of_products()

@then("Verify that products displayed are within the Price filter")
def verify_price_filter(context):
    context.app.main_page.verify_price_within_range()
