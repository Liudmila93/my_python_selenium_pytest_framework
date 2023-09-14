import time
import allure
from locators.login_page_locators import *
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Some parameters are private __"""
    __login_url = f"https://www.beerwulf.com/en-nl/my-account/Login?ReturnUrl=/en-NL/AccountInformation/OrderHistory"

    def open_page(self):
        self._open(self.__login_url)

    @allure.step("Enter user name")
    def enter_user_name(self, username: str):
        self._is_element_visible(*LoginPageLocators.USER_NAME_INPUT)
        username_locator = self._browser.find_element(*LoginPageLocators.USER_NAME_INPUT)
        username_locator.send_keys(username)

    @allure.step("Enter password")
    def enter_password(self, password: str):
        self._is_element_visible(*LoginPageLocators.USER_PASSWORD_INPUT)
        password_locator = self._browser.find_element(*LoginPageLocators.USER_PASSWORD_INPUT)
        password_locator.send_keys(password)

    @allure.step("Press Log In button")
    def press_log_in(self):
        self._is_element_visible(*LoginPageLocators.LOGIN_BTN)
        submit_button_locator = self._browser.find_element(*LoginPageLocators.LOGIN_BTN)
        submit_button_locator.click()
        time.sleep(2)

    @allure.step("Accept 18 age disclaimer")
    def accept_eighteen(self):
        try:
            yes_for_eighteen = self._browser.find_element(*LoginPageLocators.EIGHTEEN_YES)
            yes_for_eighteen.click()
        except:
            pass

    def is_error_message_visible(self) -> bool:
        return self._is_element_visible(*LoginPageLocators.ERROR_MSG)

    def is_error_message_displayed_correctly(self) -> bool:
        return self._is_text_present(*LoginPageLocators.ERROR_MSG, "No account exists with the combination of this e-mail address and password")