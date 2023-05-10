from splinter.browser import Browser
from selenium.webdriver import ChromeOptions


def before_all(context):
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    context.browser = Browser('chrome', options=options)


def after_all(context):
    context.browser.quit()
    context.browser = None
