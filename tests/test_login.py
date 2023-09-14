import pytest
import allure
import os
from dotenv import load_dotenv
from pages.logged_in_succesfully import LoggedInSuccessfullyPage
from pages.login_page import LoginPage

"""Environment variables loaded from .env file"""


@allure.feature("Login page functionality")
class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    @allure.step("Login with valid username and password")
    def test_positive_login(self, open_browser):
        # Go to webpage
        login_page = LoginPage(open_browser)
        login_page.open_page()

        # Accept disclaimer
        login_page.accept_eighteen()

        # Login
        load_dotenv()
        login_page.enter_user_name(os.getenv("LOGIN"))
        login_page.enter_password(os.getenv("PASSWORD"))
        login_page.press_log_in()

        # Assertion
        logged_in_page = LoggedInSuccessfullyPage(open_browser)
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not the same as expected"
        assert logged_in_page.is_user_logged_in_icon_displayed(), "Logout button should be visible"
        assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible"


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @allure.step("Login with invalid username and password")
    @pytest.mark.parametrize("user_mail, user_password", [("incorrect_user@gmail.com", "test1234!"), ("ludo4ka.th@mail.ru", "incorrect_password")])
    def test_negative_login(self, open_browser, user_mail, user_password):
        # Go to webpage
        login_page = LoginPage(open_browser)
        login_page.open_page()

        login_page.accept_eighteen()

        login_page.enter_user_name(user_mail)
        login_page.enter_password(user_password)
        login_page.press_log_in()

        assert login_page.is_error_message_visible(), "Error message is not displayed, but it should be"
        assert login_page.is_error_message_displayed_correctly(), "Error message is not expected"


