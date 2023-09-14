from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
import allure
import time


class BasePage:
    """Common methods for all pages
    Some parameters are private (underscored) - they are intended for internal use within the class containing this code
    , and they should not be accessed directly from outside the class."""
    def __init__(self, browser):
        self._browser = browser

    def _open(self, url: str):
        self._browser.get(url)
        time.sleep(2)

    def _find(self, locator: tuple) -> WebElement:
        return self._browser.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._is_element_visible(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple, time: int = 10):
        self._is_element_visible(locator, time)
        self._find(locator).click()

    @property
    def current_url(self) -> str:
        return self._browser.current_url

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _is_element_visible(self, how, what,
                            timeout=20) -> bool:  # два аргумента: как искать (css, id) и что искать (строку-селектор)
        try:
            WebDriverWait(self._browser, timeout).until(EC.visibility_of_all_elements_located((how, what)))
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True

    def _is_text_present(self, how, what, what_text, timeout=15) -> bool:
        try:
            WebDriverWait(self._browser, timeout).until(EC.text_to_be_present_in_element((how, what), what_text))
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._browser, time)
        wait.until(EC.visibility_of_element_located(locator))

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self._browser.get_screenshot_as_png,
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )