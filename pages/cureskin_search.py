import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from pages.base_page import Page

class CureSkinSearch(Page):
    RESULT_CONTAINER= (By.ID, "ProductGridContainer")
    NAME= (By.XPATH, "//div[@class='card-information']//a[@class='card-information__text h4']")
    IMAGE= (By. XPATH, "//lazy-image[@class='image-animate media media--portrait media--hover-effect']/img")
    PRICE= (By.CSS_SELECTOR, '.price-item.price-item--sale')

    def open_search_results_page(self):
        self.driver.get('https://shop.cureskin.com/search?q=cure')

    def verify_first_results(self):
        max_number_of_elemts = 8
        for i in range(max_number_of_elemts):
            assert self.find_elements(*self.NAME)[i]
            assert self.find_elements(*self.IMAGE)[i]
            assert self.find_elements(*self.PRICE)[i]
        # Find the search result container
        # self.driver.find_element(*self.RESULT_CONTAINER)

