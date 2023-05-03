from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class MainPage(Page):
    SHOP_ALL_SECTION = (By.CSS_SELECTOR, ".list-menu.list-menu--inline a[href*='/collections/all']")
    SLIDER_LOW = (By.CSS_SELECTOR, "div.is-lower")
    SLIDER_HIGH = (By.CSS_SELECTOR, "div.is-upper")
    PRODUCTS = (By.CSS_SELECTOR, "div.collection ul li")
    PRODUCTS_ON_PAGE = (By.CSS_SELECTOR, "ul#product-grid li")
    NEXT = (By.CSS_SELECTOR, "li a.pagination__item--prev")
    POPUP_CLOSE = (By.CSS_SELECTOR, ".popup-close")
    PRODUCTS_COUNT = (By.ID, 'ProductCount')
    ALL_PRICES = (By.CSS_SELECTOR, ".price-item.price-item--sale")
    PRICE_FILTER = (By.CSS_SELECTOR, ".facets__price > div")

    def click_shop_all(self):
        shop_all_option = self.find_element(*self.SHOP_ALL_SECTION)
        actions = ActionChains(self.driver)
        actions.move_to_element(shop_all_option).perform()
        self.wait_for_element_click(*self.SHOP_ALL_SECTION)

    def close_popup_window(self):
        self.wait_for_element_click(*self.POPUP_CLOSE)

    def adjust_price_filter(self):
        self.driver.original_number_of_products = self.find_element(*self.PRODUCTS_COUNT).text
        price_slider = self.driver.find_element(*self.SLIDER_LOW)
        actions = ActionChains(self.driver)
        actions.click_and_hold(price_slider).move_by_offset(100, 0).release().perform()
        sleep(5)

    def verify_number_of_product_changed(self):
        new_products = self.find_elements(*self.PR_PAGES)
        print(f"New product pages are {len(new_products)}")
        assert new_products != self.product_pages, "Products did not changed after adjusting the slider"

    def verify_number_of_products(self):
        current_number_of_products = self.find_element(*self.PRODUCTS_COUNT).text
        assert self.driver.original_number_of_products != current_number_of_products, \
            f'The old number of products {self.driver.original_number_of_products} is equal to the current {current_number_of_products}'

    def verify_price_within_range(self):
        # # lowest price
        # low_price = (self.find_element(*self.SLIDER_LOW)).get_attribute("aria-valuenow")
        # low_price = int(low_price[4:])
        # print(f"Low price range selected is {low_price}")
        #
        # # Highest price
        # high_price = self.find_element(*self.SLIDER_HIGH).get_attribute("aria-valuenow")
        # high_price = int(high_price[4:])
        # print(f"High price range selected is {high_price}")
        #
        # # Get products on current page
        # products_on_page = self.find_elements(*self.PRODUCTS)
        # print(f"Products on this page are {len(products_on_page)}")
        #
        # while 1:
        #     products = self.find_elements(*self.PRODUCTS_ON_PAGE)
        #
        #     for product in products:
        #         price = product.find_element(By.CSS_SELECTOR, "bdi").get_attribute("outerText")
        #         price = int(price[3:6])
        #         print(f"Price is {price}")
        #         assert low_price <= price <= high_price, "Filtered products price not in the specified range"
        #
        #     try:
        #         self.click(*self.NEXT)
        #     except:
        #         break
        #
        lowest_price = float(self.find_element(*self.PRICE_FILTER).text.replace('Price: Rs.', '').replace(' — Rs. 725', ''))
        highest_price = float(self.find_element(*self.PRICE_FILTER).text.replace('Price: Rs. 360 — Rs. ', ''))

        all_prices = self.find_elements(*self.ALL_PRICES)

        for price in all_prices:
            assert float(price.text.replace('Rs.', '')) >= lowest_price and float(price.text.replace('Rs.', '')) <= highest_price, \
                f'price {price}, not inside the range'




# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import Select
#
# from pages.base_page import Page
#
# class Cureskinhomepage(Page):
#     URL = "https://shop.cureskin.com/"
#     SHOP_ALL_SECTION= (By.XPATH, "//a[@href='/shop-all']")
#     # (By.XPATH, '//a[@class="header__menu-item header__menu-item--top list-menu__item focus-inset"]/span')
#     # PRICE_RANGE= (By.XPATH, '//div[@class="price-range__track-wrapper"]')
#     PRICE_FILTER_MIN= (By.XPATH, "//input[@id='price-min']")
#     PRICE_FILTER_MAX= (By.XPATH, "//input[@id='price-maz']")
#     PRODUCT_LIST= (By.XPATH, "//div[@id='product-list']div")
#     PRODUCT_PRICE= (By.XPATH, ".//div[@class='product-price']div")
#
#
#
#     def open_cureskin_homepe(self):
#     self.driver.get(self.'https://shop.cureskin.com/')
#
#
#
# def click_shop_all(self):
#     shop_all_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SHOP_ALL_SECTION))
#     shop_all_button.click()
#
#
# # @then('Adjust the Price Filter such that there is a change in number of products')
# def adjust_price_filter(self, min_price, max_price):
#     min_price_input = self.driver.find_element(*self.PRICE_FILTER_MIN)
#     max_price_input = self.driver.find_element(*self.PRICE_FILTER_MAX)
#     min_price_input.clear()
#     min_price_input.send_keys(str(min_price))
#     max_price_input.clear()
#     max_price_input.send_keys(str(max_price))
#
#
#
# # @then("Verify that number of products changes")
# def verify_product_number_change(self):
#     return self.driver.find_elements(*self.PRODUCT_LIST)
#
#
#
# # @then("Verify that products displayed are within the Price filter")
# def verify_price_filter(self):
