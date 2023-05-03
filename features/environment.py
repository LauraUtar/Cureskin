from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from app.application import Application


# Allure command:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature


def browser_init(context):
    """
    :param context: Behave context
    """
    #context.driver = webdriver.Chrome(executable_path="/chromedriver")
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("window-size=1400,2100")
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--headless')
    # context.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/chromdriver")
    # context.driver = webdriver.Safari()
    # context.driver = webdriver.Firefox(executable_path="/geckodriver")

    # ############# FIREFOX #############################
    # context.browser = webdriver.Firefox()
    # options = Options()
    # options.headless = True
    # options.add_argument("-private")
    # context.driver = webdriver.Firefox(options=options, executable_path="./geckodriver")
    # #####################################################

    ########### BROWSERSTACK #######################################
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'laurautarbayeva_5Qur3j'
    bs_key = 'PXazetPpJMV2Kx1NYmgH'

    desired_cap = {
        'browserName': 'Firefox',
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10'
        }
    }
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    ###################################################################

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(driver=context.driver)

    # behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_search.feature

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
