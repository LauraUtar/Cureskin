from pages.cureskin_search import  Cureskin_Search

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.cureskin_search = Cureskin_Search(self.driver)