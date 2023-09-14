from selenium.webdriver.remote.webdriver import WebDriver
from locators.login_page_locators import *
from pages.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    _logged_in_url = "https://www.beerwulf.com/en-NL/AccountInformation/OrderHistory"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self._logged_in_url

    def is_logout_button_displayed(self) -> bool:
        return self._is_element_visible(*LoginPageLocators.LOGOUT_BTN)

    def is_user_logged_in_icon_displayed(self) -> bool:
        return self._is_element_visible(*LoginPageLocators.LOGGED_IN_ICON)