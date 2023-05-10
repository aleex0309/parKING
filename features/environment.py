from splinter.browser import Browser

chrome_options = ['--no-sandbox']


def before_all(context):
    context.browser = Browser('chrome', headless=True, options=chrome_options)


def after_all(context):
    context.browser.quit()
    context.browser = None
