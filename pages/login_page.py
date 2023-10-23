from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Login page locators
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'submit-button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'h3[data-test="error"]')

    # Input username
    def fill_username_field(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    # Input password
    def fill_password_field(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    # Click "Login" button
    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # Check that error message displays
    def is_error_message_displayed(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).is_displayed()

    # Get error message text
    def get_error_message_text(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text

    # Fill login form and log in
    def login(self, username, password):
        self.fill_username_field(username)
        self.fill_password_field(password)
        self.click_login()