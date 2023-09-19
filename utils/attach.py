import allure
from allure_commons.types import AttachmentType


def add_screenshot(my_driver):
    png = my_driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(my_driver):
    log = "".join(f'{text}\n' for text in my_driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(my_driver):
    html = my_driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')
