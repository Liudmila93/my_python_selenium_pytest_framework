from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER_NAME_INPUT = (By.CSS_SELECTOR, "[name='Email']")
    USER_PASSWORD_INPUT = (By.CSS_SELECTOR, "[name='Password']")
    LOGIN_BTN = (By.XPATH, "//button[text()='Log in']")
    ERROR_MSG = (By.CSS_SELECTOR, "span[for ='Password']")
    EIGHTEEN_YES = (By.ID, "eighteenTrigger")


    # Logged in
    LOGOUT_BTN = (By.XPATH, "//div[@class='account-sidebar']//a[text()='Log out'] ")
    LOGGED_IN_ICON = (By.CSS_SELECTOR, "a.menu-icon.logged-in")


